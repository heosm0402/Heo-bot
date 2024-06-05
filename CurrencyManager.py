import logging
from datetime import datetime, timedelta

import requests

import CONSTANT as CONST


class CurrencyManager:
    def __init__(self, currency):
        self.logger = logging.getLogger("main")
        self.last_updated_utc = None
        self.last_updated_kst = None
        self.price = None
        self.direction = None
        self.direction_emoji = None
        self.currency = currency
        self.update_currency_detail()

    def get_only_base_price(self):
        resp = self.get_currency_detail()
        return resp.get("basePrice")

    def get_currency_detail(self):
        return requests.get(f"https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRW{self.currency}").json()[0]

    def update_currency_detail(self):
        resp = self.get_currency_detail()
        self.logger.info(resp)
        current_price = resp.get("basePrice")
        if self.price is None:
            self.price = current_price
        if self.price > current_price:
            self.direction_emoji = "📉"
        elif self.price < current_price:
            self.direction_emoji = "📈"
        else:
            self.direction_emoji = "🔒"

        self.price = current_price
        self.last_updated_utc: datetime = datetime.strptime(resp.get("modifiedAt"), "%Y-%m-%dT%H:%M:%S.000+00:00")
        self.last_updated_kst = self.last_updated_utc.astimezone(CONST.KST) - timedelta(hours=9)
        self.direction = resp.get("change")

    def get_currency_detail_for_message(self):
        self.update_currency_detail()
        r = f"{(datetime.now().astimezone(CONST.KST) + timedelta(hours=9)).strftime('%Y-%m-%d %H:%M:%S')} | " \
               f"{self.last_updated_kst.strftime('%Y-%m-%d %H:%M:%S')} | " \
               f"{self.currency}: {self.price} {self.direction_emoji}"
        self.logger.info(f"detail for message: {r}")
        return r
