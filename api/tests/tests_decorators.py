import logging

from .base import BaseAuthenticationTestCase
from api.decorators import authenticate_application
from clients.models import Client
from django.urls import reverse_lazy
from rest_framework.test import APIClient


class Fx():

    def __init__(self, request):
        self.request = request

    def x(self, request, *args, **kwargs):
        return request

    __call__ = x


class DecoratorsTestCase(BaseAuthenticationTestCase):

    """Test the authoriation decorator

    Attributes:
        client (model): A client
        factory (request): Request builder
        url (str): The url to test
    """

    def setUp(self):
        """Initialize the vars for the test
        """
        self.client = Client.objects.create(username="test", password="test")
        self.client.set_password("test")
        self.client.save()
        self.url = reverse_lazy("login")
        self.url_profile = reverse_lazy("profile")
        self.token = None

        self.api_client = APIClient()

    def test_oauth_decorator_authentication_required(self):
        """Should validate and requires the authorization header
        """

        request = self.api_client.post(
            self.url, {
                "username": self.client.username,
                "password": "test"
            },
            format="json",
            HTTP_AUTHORIZATION=""
        )

        expected_answer = {
            "error_code": "AUTHENTICATION_REQUIRED",
            "errors": {"authorization": "Missing authorization"}
        }
        self.assertEquals(expected_answer, request.data)

    def test_oauth_decorator_invalid_bearer_encode(self):
        """Should validate a bad base64 encoded bearer
        """
        request = self.api_client.post(
            self.url, {
                "username": self.client.username,
                "password": "test"
            },
            format="json",
            HTTP_AUTHORIZATION="Bearer a"
        )

        expected_answer = {
            "error_code": "BAD_BEARER",
            "errors": {
                "bearer": "Bad authorization bearer"
            }
        }
        self.assertEquals(expected_answer, request.data)

    def test_oauth_decorator_invalid_bearer_split(self):
        """Should validate a bad bearer
        """

        request = self.api_client.post(
            self.url, {
                "username": self.client.username,
                "password": "test"
            },
            format="json",
            HTTP_AUTHORIZATION="{}".format(
                self.generate_bad_bearer_header("oi", "oi:oi").get(
                    "HTTP_AUTHORIZATION").decode("utf-8"))
        )

        expected_answer = {
            "error_code": "BAD_BEARER",
            "errors": {
                "bearer": "Bad authorization bearer"
            }
        }
        self.assertEquals(expected_answer, request.data)

    def test_oauth_decorator_invalid_application(self):
        """Should validate a invalid application
        """

        request = self.api_client.post(
            self.url, {
                "username": self.client.username,
                "password": "test"
            },
            format="json",
            HTTP_AUTHORIZATION="{}".format(
                self.generate_bad_bearer_header("oi", "oi").get(
                    "HTTP_AUTHORIZATION").decode("utf-8"))
        )

        expected_answer = {
            "error_code": "INVALID_APPLICATION",
            "errors": {"application": "Invalid application"}
        }
        self.assertEquals(expected_answer, request.data)

    def test_oauth_decorator_success(self):
        """Should succeed on token generation
        """

        request = self.api_client.post(
            self.url, {
                "username": self.client.username,
                "password": "test"
            },
            format="json",
            HTTP_AUTHORIZATION="{}".format(
                self.generate_bearer_header().get(
                    "HTTP_AUTHORIZATION").decode("utf-8"))
        )

        self.assertIn("token", str(request.data))

    def test_oauth_decorator_invalid_token(self):
        """Should validate a bad base64 encoded bearer
        """
        request = self.api_client.post(
            self.url, {
                "username": self.client.username,
                "password": "test"
            },
            format="json",
            HTTP_AUTHORIZATION="Token a"
        )

        expected_answer = {
            "error_code": "INVALID_TOKEN",
            "errors": {
                "token": "Invalid token"
            }
        }
        self.assertEquals(expected_answer, request.data)

    def test_oauth_decorator_valid_token(self):
        """Should validate a bad base64 encoded bearer
        """

        request = self.api_client.post(
            self.url, {
                "username": self.client.username,
                "password": "test"
            },
            format="json",
            HTTP_AUTHORIZATION="{}".format(
                self.generate_bearer_header().get(
                    "HTTP_AUTHORIZATION").decode("utf-8"))
        )

        self.token = request.data.get("token")

        request = self.api_client.get(
            self.url_profile,
            HTTP_AUTHORIZATION="Token " + self.token
        )

        expected_answer = {"credit": 0,
                           "first_name": "",
                           "last_name": "",
                           "savings": 0,
                           "username": "test"}
        self.assertEquals(expected_answer, request.data)

    def test_oauth_decorator_invalid_header(self):
        """Should validate a bad base64 encoded bearer
        """
        request = self.api_client.post(
            self.url, {
                "username": self.client.username,
                "password": "test"
            },
            format="json",
            HTTP_AUTHORIZATION="Banana"
        )

        expected_answer = {
            "error_code": "MISSING_AUTHORIZATION",
            "errors":
            {
                "bearer": "Invalid Bearer",
                "token": "Invalid Token",
            }
        }
        self.assertEquals(expected_answer, request.data)
