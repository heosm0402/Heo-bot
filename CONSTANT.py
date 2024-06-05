import os

import pendulum


KST = pendulum.timezone("Asia/Seoul")
SLACK_CURRENCY_CHANNEL_NAME = "알람-환율"
CURRENCY_REQUEST_URL = ""
TOKEN = os.environ.get("BOT_USER_OAUTH_TOKEN")
PROJECT_ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
LOG_ROOT_DIR = os.path.join(PROJECT_ROOT_DIR, "logs/")