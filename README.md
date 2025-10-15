# Basement Dweller
A script that keeps your **Reddit Streak 🔥** alive ... yup it runs every day without you doing anything!

**⚠️ For educational and demonstrative purposes only. Any losses or problems with your account that may arise from using it are your responsibility. Consider using a different account if you intend to run it, as doing so could result in account getting banned.**

## Setup (with Docker)

### Requirements
- [Docker](https://www.docker.com/)


### Steps
1. Setup environment variables following [Environment Variables](#environment-variables) guide.

3. Run a docker container:
    ```
    docker-compose up
    ```


## Manual Setup

### Requirements
- [Python 3.7+](https://python.org/downloads)

### Steps

1. Copy the files and folder manually or using [Git](https://git-scm.com/), and open it.

2. Setup environment variables following [Environment Variables](#environment-variables) guide.

3. Install all the dependencies:
    ```
    pip install -r src/requirements.txt
    ```

4. Install chromium:
    ```
    playwright install --with-deps chromium
    ```

5. Run the script:
    ```
    python src/main.py
    ```

## Environment Variables
Go to `.env` file and update all the variables as:
- **EMAIL**: Your reddit account email or password.
- **PASSWORD**: Your reddit account password.

```
EMAIL=abc@gmail.com
PASSWORD=abcdefghijk
```