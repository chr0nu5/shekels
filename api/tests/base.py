"""Authentication tests."""
import base64
import simplejson as json

from oauth.models import OAuthApplication
from rest_framework.test import APITestCase


class BaseAuthenticationTestCase(APITestCase):
    """Base test class."""

    def generate_custom_bearer_header(self, key, secret):
        auth = '{id}:{secret}'.format(id=key, secret=secret)
        auth = bytes(auth, 'utf-8')
        return {
            'HTTP_AUTHORIZATION': b'Bearer %s' % base64.b64encode(auth)
        }

    def generate_bad_bearer_header(self, key, secret):
        auth = '{id}:{secret}'.format(id=key, secret=secret)
        auth = bytes(auth, 'utf-8')
        return {
            'HTTP_AUTHORIZATION': b'Bearer %s' % base64.b64encode(auth)
        }

    def generate_bad_token_header(self, key, secret):
        auth = '{id}:{secret}'.format(id=key, secret=secret)
        auth = bytes(auth, 'utf-8')
        return {
            'HTTP_AUTHORIZATION': b'Token %s' % base64.b64encode(auth)
        }

    def generate_bearer_header(self):
        a = OAuthApplication()
        a.name = 'shekels'
        a.description = 'shekels'
        keys = a.hash_keys()
        client_id = keys['key']
        client_secret = keys['secret']
        auth = '{id}:{secret}'.format(id=client_id, secret=client_secret)
        auth = bytes(auth, 'utf-8')
        return {
            'HTTP_AUTHORIZATION': b'Bearer %s' % base64.b64encode(auth)
        }

    def generate_token_header(self, token):
        return {
            'HTTP_AUTHORIZATION': 'Token {}'.format(token)
        }
