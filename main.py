import logging
import os.path
import time
import argparse
from datetime import datetime, timedelta

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

import utils
from CurrencyManager import CurrencyManager
import CONSTANT as CONST
from utils import return_interval_to_seconds

os.environ["TZ"] = "Asia/Seoul"


def send_message(channel, msg):
    logger = logging.getLogger("main")
    client = WebClient(token=CONST.TOKEN)
    try:
        result = client.chat_postMessage(
            channel=channel,
            text=msg
        )
        logger.info(f"slack send result: {result}")
    except SlackApiError as e:
        logger.info(f"SlackApiError: {e}")


def main(args):
    logger = logging.getLogger("main")
    manager = CurrencyManager(args.currency)
    interval = return_interval_to_seconds(args.interval)
    logger.info(f"seconded interval: {interval}s")

    while 1:
        send_message(CONST.SLACK_CURRENCY_CHANNEL_NAME, manager.get_currency_detail_for_message())
        time.sleep(interval)


if __name__ == '__main__':
    logger_main = utils.get_log_handler("main", logging.INFO, os.path.join(CONST.LOG_ROOT_DIR, "main.log"))
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", dest="currency", required=True)
    parser.add_argument("-i", dest="interval", required=False, default="60")
    main(parser.parse_args())
