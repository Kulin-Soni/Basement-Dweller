# ⚠️ This script is only for educational and demonstrative purposes only. Any losses or problems with your account that may arise from using it are your responsibility. Consider using a different account if you intend to run it, as doing so could result in account getting banned.

from time import sleep, time
from playwright.async_api import async_playwright, BrowserContext, Page
from threadFunction import threadFn
from random import randint
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

# Constants -
REDDIT_HOME = "https://www.reddit.com"
USERNAME = os.getenv("EMAIL", "")
PASSWORD = os.getenv("PASS", "")
DAY_IN_SECONDS = 24 * 60 * 60
#

# Gives a random time in seconds after the current day passes by.
async def getDelay():
    day_left = (DAY_IN_SECONDS) - int(time()) % (DAY_IN_SECONDS)
    delay = randint(3600, DAY_IN_SECONDS - 3600) + day_left
    return delay


# Launcher for upvote job -
async def launchUpvoteJob():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context()   
        while True:
            print("[LOG] RUNNING SCHEDULED JOB")
            delay = getDelay()
            job = await upvotePost(browser=ctx)
            if not job: break
            sleep(delay) # type: ignore if you're using typings.
#

# Deep search utility function -
async def deepSearch(page: Page, query: str):
    '''Automatically finds the first instance of query in all the documents roots.
    We are using this function because Reddit uses multiple shadow dom.
    '''
    deep_search_fn = f'''
    (()=>{{function querySelectorDeep(s, r = document) {{
        let res = r.querySelector(s);
        if (res) return res;
        for (const el of r.querySelectorAll("*"))
        if (el.shadowRoot && (res = querySelectorDeep(s, el.shadowRoot))) return res;
        return null;
    }}   
    return querySelectorDeep("{query}")}})();
    '''
    btn = await page.evaluate_handle(deep_search_fn)
    return btn.as_element()
#

# Login into your reddit account -
async def loginReddit(browser: BrowserContext):
    '''Login into your Reddit account. Generally used on the first instance after running. Returns whether successfully logged in.'''

    # Open the login page
    page = await browser.new_page()
    await page.goto(f"{REDDIT_HOME}/login")

    sleep(3)

    # Query all the necessary elements -
    userNameInput = await deepSearch(page=page, query="input[name='username']")
    passwordInput = await deepSearch(page=page, query="input[name='password']")
    submitBtn = await deepSearch(page=page, query="button.login")

    if userNameInput and passwordInput and submitBtn:

        await userNameInput.fill(USERNAME)
        await passwordInput.fill(PASSWORD)
        sleep(.5)
        await submitBtn.click()

        sleep(3)
        await page.reload()

        if not (page.url==REDDIT_HOME or page.url==f"{REDDIT_HOME}/"):
            print("[LOG] INVALID USERNAME & PASSWORD")
            await page.close()
            return False
        
        print("[LOG] LOGGED INTO ACCOUNT")
        await page.close()
        return True
    

    # If couldn't track/query elements
    print("[ERR] COULDN'T TRACK ELEMENTS")
    await page.close()
    return False
#

# Up-vote post -
async def upvotePost(browser: BrowserContext):
    '''Up-votes the first post on Reddit's home page.'''
    # Open Reddit -
    page = await browser.new_page()
    async def close(ret: bool):
        await page.close()
        print("[LOG] SCHEDULED JOB FINISHED\n")
        return ret
    await page.goto(REDDIT_HOME)

    await page.reload()
    # If not logged in -
    loginBtn = page.locator("#login-button")
    if await loginBtn.count() > 0:
        loggedIn = await loginReddit(browser)
        if not loggedIn:
            return await close(False)
    
    # After logged in -
    await page.reload()
    upvoteBtn = await deepSearch(page=page, query="button[upvote]")
    if upvoteBtn:
        await upvoteBtn.click() # Click the upvote button
        print("[LOG] UPVOTED A POST")
    
    return await close(True)
#


if __name__ == "__main__":
    print("[LOG] LAUNCHING INITIAL SETUP")
    threadFn(asyncio.run(launchUpvoteJob()))  