import datetime
import glob
import pep8
import simplejson as json

from api.responses import api_error
from api.responses import api_success
from api.serializers import json_serializer

from django.test import TestCase


class ResponsesTestCase(TestCase):

    """Test the API generic responses
    """

    def setUp(self):
        """
        """
        pass

    def test_api_success(self):
        """A success response should be returned
        """
        response = api_success({"success": True})

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {"success": True}
        )

    def test_api_error(self):
        """A success response should be returned
        """
        response = api_error(None,
                             'INVALID_JSON_REQUEST',
                             status_code=400)

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'error': 'INVALID_JSON_REQUEST',
             'error_description': 'Request does not have a valid JSON'}
        )


class SerializersTestCase(TestCase):

    """Test the custom serializer
    """

    def setUp(self):
        """Create a date for testing
        """
        self.date = datetime.datetime.now()

    def test_json_serializer(self):
        """Should be able to serialize a date object
        """

        response = json.dumps(
            {"date": self.date},
            default=json_serializer)

        self.assertJSONEqual(response, {"date": str(self.date.isoformat())})


class Pep8TestCase(TestCase):

    """Test all the files for PEP8

    Attributes:
        path (str): the base path for the files
        pep8style (pep8): the checker
    """

    def setUp(self):
        """Initialize the vars for the test
        """
        self.path = '/app/'
        self.pep8style = pep8.StyleGuide(quiet=True)

    def test_pep8(self):
        """Should not show any erros"""

        for file in glob.glob('/app/' + '/**/*.py', recursive=True):
            if '/app/env/' not in file and '/migrations/' not in file:
                print(file)
                fchecker = pep8.Checker(file, show_source=True)
                file_errors = fchecker.check_all()
                self.assertEqual(file_errors, 0)
