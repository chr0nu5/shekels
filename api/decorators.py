import base64
import hashlib

from django.views.decorators.csrf import csrf_exempt
from oauth.models import OAuthApplication
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class authenticate_application(object):
    """Decorator used to "oauth" an application
    """

    def __call__(self, f):
        def wrapped_f(self, request, *args, **kwargs):
            """Expectation if an application-based bearer token, which is
            composed by the literal "bearer " followed by the application"s
            key and secret, joined by a colon, encoded in a base64 string.
            Args:
                request (TYPE): Description
                *args: Description
                **kwargs: Description
            Returns:
                api_response: an api response with the authorization
            """
            header = self.request.META.get("HTTP_AUTHORIZATION", None)
            if not header:
                return Response({"error_code": "AUTHENTICATION_REQUIRED",
                                 "errors": {
                                     "authorization": "Missing authorization"
                                 }},
                                status=status.HTTP_400_BAD_REQUEST)

            # Check if we have to validate a bearer or a token
            if isinstance(header, bytes):
                header = header.decode("utf-8")

            if header.startswith("Bearer "):
                header = header.replace("Bearer ", "")
                token = header
                try:
                    header = base64.b64decode(header).decode()
                except Exception as e:
                    return Response({"error_code": "BAD_BEARER",
                                     "errors": {
                                         "bearer": "Bad authorization bearer"
                                     }},
                                    status=status.HTTP_400_BAD_REQUEST)
                header = header.split(":")
                if len(header) != 2:
                    return Response({"error_code": "BAD_BEARER",
                                     "errors": {
                                         "bearer": "Bad authorization bearer"
                                     }},
                                    status=status.HTTP_400_BAD_REQUEST)
                hashed_key = hashlib.sha1(header[0].encode()).hexdigest()
                hashed_secret = hashlib.sha1(header[1].encode()).hexdigest()
                obj = OAuthApplication.objects.filter(
                    key=hashed_key, secret=hashed_secret).first()
                if not obj:
                    return Response({"error_code": "INVALID_APPLICATION",
                                     "errors": {
                                         "application": "Invalid application"
                                     }},
                                    status=status.HTTP_400_BAD_REQUEST)

                self.request.application = obj
                self.request.token = token if token else ""
                return f(self, self.request, *args, **kwargs)

            elif header.startswith("Token "):
                """Validate the token an see if it´s not expired."""
                try:
                    _, request_token = header.split("Token ")
                    token = Token.objects.get(key=request_token)
                    self.request.token = token.key
                    self.request.user = token.user
                    return f(self, self.request, *args, **kwargs)
                except Token.DoesNotExist:
                    return Response({"error_code": "INVALID_TOKEN",
                                     "errors": {
                                         "token": "Invalid token"
                                     }},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error_code": "MISSING_AUTHORIZATION",
                                 "errors": {
                                     "bearer": "Invalid Bearer",
                                     "token": "Invalid Token",
                                 }},
                                status=status.HTTP_400_BAD_REQUEST)
        return csrf_exempt(wrapped_f)
