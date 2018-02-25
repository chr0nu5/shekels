from clients.models import Client
from entries.models import Entry
from rest_framework import serializers


def required(value):
    if value is None:
        raise serializers.ValidationError('This field is required')


class LoginSerializer(serializers.Serializer):

    """Client Login Serializer

    Attributes:
        password (str): the password
        username (str): the username
    """

    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)


class ProfileSerializer(serializers.Serializer):

    """Update client credit and savings

    Attributes:
        credit (float): the bank credit
        savings (float): the bank savings
    """

    first_name = serializers.CharField(validators=[required])
    last_name = serializers.CharField(validators=[required])
    credit = serializers.DecimalField(
        max_digits=9,
        decimal_places=2,
        coerce_to_string=None,
        max_value=1000000,
        min_value=0.00)
    savings = serializers.DecimalField(
        max_digits=9,
        decimal_places=2,
        coerce_to_string=None,
        max_value=1000000,
        min_value=0.00)


class RegisterSerializer(serializers.ModelSerializer):

    """Client Register Serializer

    Attributes:
        email (str): the email custom validator
        first_name (str): the first name custom validator
        last_name (str): the last name custom validator
    """

    first_name = serializers.CharField(validators=[required])
    last_name = serializers.CharField(validators=[required])
    email = serializers.CharField(validators=[required])

    class Meta:
        model = Client
        fields = ('username', 'password', 'first_name', 'last_name', 'email',)


class PasswordSerializer(serializers.Serializer):

    """Client Password Update Serializer

    Attributes:
        password (TYPE): Description
    """

    password = serializers.CharField(max_length=128)


class EntrySerializer(serializers.Serializer):

    order = serializers.IntegerField(max_value=10, min_value=1)
    date = serializers.DateTimeField()
    value = serializers.DecimalField(
        max_digits=9,
        decimal_places=2,
        coerce_to_string=None,
        max_value=1000000,
        min_value=-1000000)
    comment = serializers.CharField(
        max_length=255, allow_blank=True, allow_null=True)


class UpdateEntrySerializer(serializers.Serializer):

    value = serializers.DecimalField(
        max_digits=9,
        decimal_places=2,
        coerce_to_string=None,
        max_value=1000000,
        min_value=-1000000)
    comment = serializers.CharField(max_length=255, required=False)
