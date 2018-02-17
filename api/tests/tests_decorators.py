import logging

from .base import BaseAuthenticationTestCase
from api.decorators import authenticate_application
from clients.models import Client
from django.urls import reverse_lazy
from rest_framework.test import APIRequestFactory


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
        self.factory = APIRequestFactory()
        self.client = Client.objects.create(username="test", password="test")
        self.url = reverse_lazy('login')

    def test_oauth_decorator_success(self):
        """Should raise a TypeError
        """
        header = self.generate_bearer_header().get(
            "HTTP_AUTHORIZATION").decode("utf-8")

        request = self.factory.post(
            self.url, {
                "username": self.client.username,
                "password": self.client.password
            },
            HTTP_AUTHORIZATION='{}'.format(header)
        )

        error = None
        try:
            decorator = authenticate_application()
            response = decorator(request)
            response.request = request
            response = response(response, request)
        except Exception as e:
            error = e
        self.assertRaises(TypeError, error)

    def test_oauth_decorator_missing_bearer_token(self):
        """Should return invalid bearer and invalid token
        """
        header = None

        request = self.factory.post(
            self.url, {
                "username": self.client.username,
                "password": self.client.password
            },
            HTTP_AUTHORIZATION='{}'.format(header)
        )

        decorator = authenticate_application()
        response = decorator(request)
        response.request = request
        response = response(response, request)

        expected_answer = {
            "error_code": "MISSING_AUTHORIZATION",
            "errors": {
                "bearer": "Invalid Bearer",
                "token": "Invalid Token"}
        }
        self.assertEquals(expected_answer, response.data)

    def test_oauth_decorator_invalid_bearer(self):
        """Should return invalid bearer
        """
        header = "Bearer invalid"

        request = self.factory.post(
            self.url, {
                "username": self.client.username,
                "password": self.client.password
            },
            HTTP_AUTHORIZATION='{}'.format(header)
        )

        decorator = authenticate_application()
        response = decorator(request)
        response.request = request
        response = response(response, request)

        expected_answer = {
            "error_code": "BAD_BEARER",
            "errors": {
                "bearer": "Bad authorization bearer"
            }
        }
        self.assertEquals(expected_answer, response.data)

    def test_oauth_decorator_invalid_token(self):
        """Should return invalid token
        """
        header = "Token invalid"

        request = self.factory.post(
            self.url, {
                "username": self.client.username,
                "password": self.client.password
            },
            HTTP_AUTHORIZATION='{}'.format(header)
        )

        decorator = authenticate_application()
        response = decorator(request)
        response.request = request
        response = response(response, request)

        expected_answer = {
            "error_code": "INVALID_TOKEN",
            "errors": {
                "token": "Invalid token"
            }
        }
        self.assertEquals(expected_answer, response.data)

    def test_oauth_decorator_invalid_application(self):
        """Should return invalid token
        """
        header = self.generate_custom_bearer_header("a", "b").get(
            "HTTP_AUTHORIZATION").decode("utf-8")

        request = self.factory.post(
            self.url, {
                "username": self.client.username,
                "password": self.client.password
            },
            HTTP_AUTHORIZATION='{}'.format(header)
        )

        decorator = authenticate_application()
        response = decorator(request)
        response.request = request
        response = response(response, request)

        expected_answer = {
            "error_code": "INVALID_APPLICATION",
            "errors": {
                "application": "Invalid application"
            }
        }
        self.assertEquals(expected_answer, response.data)

    def test_oauth_decorator_invalid_bearer(self):
        """Should return invalid bearer
        """
        header = "Bearer invalid as fuck"

        request = self.factory.post(
            self.url, {
                "username": self.client.username,
                "password": self.client.password
            },
            HTTP_AUTHORIZATION='{}'.format(header)
        )

        decorator = authenticate_application()
        response = decorator(request)
        response.request = request
        response = response(response, request)

        expected_answer = {
            "error_code": "BAD_BEARER",
            "errors": {
                "bearer": "Bad authorization bearer"
            }
        }
        self.assertEquals(expected_answer, response.data)

    def test_oauth_decorator_missing_authorization(self):
        """Should return invalid bearer
        """

        request = self.factory.post(
            self.url, {
                "username": self.client.username,
                "password": self.client.password
            }
        )

        decorator = authenticate_application()
        response = decorator(request)
        response.request = request
        response = response(response, request)

        expected_answer = {
            "error_code": "AUTHENTICATION_REQUIRED",
            "errors": {
                "authorization": "Missing authorization"
            }
        }
        self.assertEquals(expected_answer, response.data)
