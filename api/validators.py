from clients.models import Client
from rest_framework import serializers


def required(value):
    if value is None:
        raise serializers.ValidationError('This field is required')


class ClientSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)


class RegisterSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(validators=[required])
    last_name = serializers.CharField(validators=[required])
    email = serializers.CharField(validators=[required])

    class Meta:
        model = Client
        fields = ('username', 'password', 'first_name', 'last_name', 'email',)


class PasswordSerializer(serializers.Serializer):

    password = serializers.CharField(max_length=128)
