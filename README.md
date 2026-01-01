# Basement Dweller
A script that keeps your **Reddit Streak 🔥** alive ... yup it runs every day without you doing anything!

**⚠️ For educational and demonstrative purposes only. Any losses or problems with your account that may arise from using it are your responsibility. Consider using a different account if you intend to run it, as doing so could result in account getting banned.**

## Setup (with Docker)

### Requirements
- [Docker](https://www.docker.com/)


### Steps
1. Setup environment variables following [Environment Variables](#environment-variables) guide.

3. Build & run a docker container:
    ```
    docker build -t image_name .
    docker run --env-file .env image_name
    ```


## Manual Setup

### Requirements
- [Python 3.7+](https://python.org/downloads)

### Steps

1. Copy the files and folder manually or using [Git](https://git-scm.com/), and open it.

2. Setup environment variables following [Environment Variables](#environment-variables) guide.

3. Run the following commands:
    ```
    pip install -r src/requirements.txt # Installs necessary dependencies.
    playwright install --with-deps chromium # Installs chromium.
    python src/main.py # Runs the script.
    ```

## Environment Variables
Go to `.env` file and update all the variables as:
- **EMAIL**: Your reddit account email or username.
- **PASS**: Your reddit account password.

```
EMAIL=abc@gmail.com
PASS=abcdefghijk
```