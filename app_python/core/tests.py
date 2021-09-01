from datetime import datetime

import pytz
from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APIRequestFactory, APITestCase


class TimeTestCase(APITestCase):

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.url = reverse('time-api')
        self.default_timezone = 'Europe/Moscow'

    def test_time_is_valid(self):
        """
        TestCase: Just checks that API is working properly with default timezone
        classification: usability
        use-case: as an application user I want to check correct time in order to do daily things
        precondition: working application
        steps: pass request with no parameters to HTTP endpoint
        expected result: response 200, with correct date and defined timezone
        """
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, 200, f"{self.url} response is not 200")
        self.assertTrue('datetime' in response.data, f"no 'datetime' field in response")
        self.assertTrue('timezone' in response.data, f"no 'timezone' field in response")
        self.assertEqual(response.data['timezone'], self.default_timezone, f"Default timezone is not {self.default_timezone}")
        moscow_time_from_api = datetime.fromisoformat(response.data['datetime'])
        moscow_time_from_test = datetime.now(pytz.timezone(self.default_timezone))
        self.assertTrue((moscow_time_from_api - moscow_time_from_test).seconds < 10, f"Time difference is more than 10 seconds: {moscow_time_from_api} from api, {moscow_time_from_test} from test ")

    def test_time_invalid_timezone(self):
        """
        TestCase: invalid timezone will result in validation error
        classification: reliability
        use-case: as an application user I want to check correct time in order to do daily things, and if I make a mistake defining time zone I will be notified
        precondition: working application
        steps: pass request with invalid timezone to API
        expected result: response 400, validation error which invalid timezone info
        """
        response = self.client.get(self.url, {'timezone': "someinvalid/timezone"}, format='json')
        self.assertEqual(response.status_code, 400, f"{self.url} response is not 400")
        self.assertTrue('timezone' in response.data, f"{self.url} response is not 400")
        self.assertTrue('unknown' in response.data['timezone'].lower(), f"{self.url} response is not 400")
