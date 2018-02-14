import hashlib

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from oauth.constants import OAuthConstants


class OAuthApplication(models.Model):

    """Model that holds the clients for the environment

    Attributes:
        application_type (int): application behavior
        APPLICATION_TYPES (obj): list of application types
        created_date (TYPE): Description
        description (str): application description
        EXTERNAL (int): an external application
        hashed_key (str): the hashed application key
        hashed_secret (str): the hashed application key
        INTERNAL (int): an internal application
        key (str): application key
        modified_date (TYPE): Description
        name (str): application name
        secret (str): application secret
    """

    INTERNAL = 0
    EXTERNAL = 1
    APPLICATION_TYPES = {
        INTERNAL: 'Internal',
        EXTERNAL: 'External',
    }

    def __init__(self, *args, **kwargs):
        """Initialize the model

        Args:
            *args: none for now
            **kwargs: none for now
        """
        models.Model.__init__(self, *args, **kwargs)
        self.hashed_key = None
        self.hashed_secret = None

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    application_type = models.IntegerField(
        choices=APPLICATION_TYPES.items(), default=EXTERNAL)
    key = models.CharField(max_length=255, blank=False, null=False,
                           db_index=True, unique=True)
    secret = models.CharField(max_length=255, blank=False, null=False,
                              db_index=True, unique=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True,
                                        null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def hash_keys(self):
        """Hide the keys on
        """
        key = OAuthConstants.generate_application_key()
        secret = OAuthConstants.generate_application_secret()
        self.key = hashlib.sha1(str.encode(key)).hexdigest()
        self.secret = hashlib.sha1(str.encode(secret)).hexdigest()
        self.save()

        return {"key": key, "secret": secret}
