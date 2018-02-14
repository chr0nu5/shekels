import base64
import hashlib

from django.views.decorators.csrf import csrf_exempt
from oauth.models import OAuthApplication
from rest_framework import status
from rest_framework.response import Response


class authenticate_application(object):
    """Decorator used to "oauth" an application

    Deleted Attributes:
        client_type (int): the application type
    """

    def __call__(self, f):
        def wrapped_f(self, request, *args, **kwargs):
            """Expectation if an application-based bearer token, which is
            composed by the literal "bearer " followed by the application's
            key and secret, joined by a colon, encoded in a base64 string.

            Args:
                request (TYPE): Description
                *args: Description
                **kwargs: Description

            Returns:
                api_response: an api response with the authorization
            """
            header = self.request.META.get('HTTP_AUTHORIZATION', None)
            if not header:
                return Response({'error_code': 'AUTHENTICATION_REQUIRED',
                                 'error': 'Missing authorization'},
                                status=status.HTTP_400_BAD_REQUEST)

            if isinstance(header, bytes):
                header = header.decode('utf-8')

            if header.startswith('bearer '):
                header = header.replace('bearer ', '')
                token = header
                try:
                    header = base64.b64decode(header).decode()
                except Exception as e:
                    return Response({'error_code': 'INVALID_BEARER',
                                     'error': 'Invalid Bearer'},
                                    status=status.HTTP_400_BAD_REQUEST)
                header = header.split(':')
                if len(header) != 2:
                    return Response({'error_code': 'INVALID_BEARER',
                                     'error': 'Invalid Bearer'},
                                    status=status.HTTP_400_BAD_REQUEST)

                hashed_key = hashlib.sha1(header[0].encode()).hexdigest()
                hashed_secret = hashlib.sha1(header[1].encode()).hexdigest()
                obj = OAuthApplication.objects.filter(
                    key=hashed_key, secret=hashed_secret).first()

                if not obj:
                    return Response({'error_code': 'INVALID_APPLICATION',
                                     'error': 'Invalid application'},
                                    status=status.HTTP_400_BAD_REQUEST)

                self.request.application = obj
                return f(self, self.request, *args, **kwargs)

            else:
                return Response({'error_code': 'MISSING_AUTHORIZATION',
                                 'error': 'Bearer Or Token not provided'},
                                status=status.HTTP_400_BAD_REQUEST)
        return csrf_exempt(wrapped_f)
