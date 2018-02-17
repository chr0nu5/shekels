import logging

from .models import Client
from api.decorators import authenticate_application
from api.validators import ClientSerializer
from api.validators import FundsSerializer
from api.validators import PasswordSerializer
from api.validators import RegisterSerializer
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework import views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class RegisterView(views.APIView):

    @authenticate_application()
    def post(self, request, *args, **kwargs):
        """Register a new client

        Args:
            request (TYPE): Description
            *args: Description
            **kwargs: Description

        Returns:
            JSON: response
        """
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            client = Client(
                username=request.data.get("username"),
                password=request.data.get("password"),
                first_name=request.data.get("first_name"),
                last_name=request.data.get("last_name"),
                email=request.data.get("email")
            )
            client.set_password(request.data.get("password"))
            client.save()
            return Response({})
        else:
            return Response({
                "error_code": "INVALID_REGISTRATION",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):

    @authenticate_application()
    def post(self, request, *args, **kwargs):
        """Login a client

        Args:
            request (TYPE): Description
            *args: Description
            **kwargs: Description

        Returns:
            JSON: response
        """

        serializer = ClientSerializer(data=request.data)

        if serializer.is_valid():
            client = authenticate(
                username=request.data.get("username"),
                password=request.data.get("password"))

            if client is not None:
                token, created = Token.objects.get_or_create(user=client)
                if not created:
                    token.delete()
                    token = Token.objects.create(user=client)
                return Response({
                    "token": token.key
                })
            else:
                return Response({
                    "error_code": "UNAUTHORIZED",
                    "errors": {
                        "username": "Invalid username",
                        "password": "Invalid password"
                    }
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                "error_code": "INVALID_DATA",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(views.APIView):

    @authenticate_application()
    def get(self, request, *args, **kwargs):
        """Get a user profile

        Args:
            request (TYPE): Description
            *args: Description
            **kwargs: Description

        Returns:
            JSON: response
        """
        client = Client.objects.get(username=self.request.user.username)

        return Response({
            "username": client.username,
            "first_name": client.first_name,
            "last_name": client.last_name,
            "credit": client.credit,
            "savings": client.savings
        })


class UpdatePasswordView(views.APIView):

    @authenticate_application()
    def put(self, request, *args, **kwargs):
        """Update a user password

        Args:
            request (TYPE): Description
            *args: Description
            **kwargs: Description

        Returns:
            JSON: response
        """

        serializer = PasswordSerializer(data=request.data)

        if serializer.is_valid():
            client = Client.objects.get(username=self.request.user.username)
            client.set_password(request.data.get("password"))
            client.save()
            return Response({})
        else:
            return Response({
                "error_code": "INVALID_UPDATE",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class UpdateFundsView(views.APIView):

    @authenticate_application()
    def put(self, request, *args, **kwargs):
        """Update a user credit and savings

        Args:
            request (TYPE): Description
            *args: Description
            **kwargs: Description

        Returns:
            JSON: response
        """

        serializer = FundsSerializer(data=request.data)

        if serializer.is_valid():
            client = Client.objects.get(username=self.request.user.username)
            client.credit = request.data.get("credit")
            client.savings = request.data.get("savings")
            client.save()
            return Response({})
        else:
            return Response({
                "error_code": "INVALID_FUNDS_UPDATE",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
