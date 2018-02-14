import datetime
import logging
import pytz

from dateutil.parser import parse


class TimeZoneHelper:

    def __init__(self):
        self.timezone = pytz.timezone('America/Sao_Paulo')

    def to_br(self, date):
        try:
            if isinstance(date, str):
                date = parse(date)
            logging.info("Will try to convert {}".format(date))
            date = datetime.datetime.combine(
                date, datetime.datetime.min.time())
            date = pytz.timezone('UTC').localize(date, is_dst=None)
            logging.info("Converted date {}".format(
                date.astimezone(self.timezone)))
            return date.astimezone(self.timezone)
        except Exception as e:
            logging.error(e)
            logging.error("Error converting date {}".format(date))
        return date
