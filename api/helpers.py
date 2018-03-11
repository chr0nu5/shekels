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
            date = datetime.datetime.combine(
                date, datetime.datetime.min.time())
            date = pytz.timezone('UTC').localize(date, is_dst=None)
            return date.astimezone(self.timezone)
        except Exception as e:
            pass
        return date
