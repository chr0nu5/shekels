import logging

from .base import BaseAuthenticationTestCase
from api.helpers import TimeZoneHelper


class HelpersTestCase(BaseAuthenticationTestCase):

    def test_timezone_valid_date(self):
        """Should return a converted time
        """
        timezone = TimeZoneHelper()
        date = timezone.to_br("2018-01-01 00:00:00")
        self.assertEquals(str(date), "2017-12-31 22:00:00-02:00")

    def test_timezone_invalid_date(self):
        """Should not return a converted time
        """
        timezone = TimeZoneHelper()
        date = timezone.to_br("banana")
        self.assertEquals(str(date), "banana")
