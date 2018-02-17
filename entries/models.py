from clients.models import Client
from django.db import models

# Create your models here.


class Entry(models.Model):

    user = models.ForeignKey(Client)
    order = models.IntegerField()
    date = models.DateTimeField()
    comment = models.CharField(max_length=255,
                               null=True,
                               blank=True)
    created_date = models.DateTimeField(auto_now_add=True,
                                        blank=True,
                                        null=True)
    modified_date = models.DateTimeField(auto_now=True,
                                         blank=True,
                                         null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"
