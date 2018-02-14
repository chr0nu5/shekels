from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)
    credit = models.DecimalField(max_digits=30,
                                 decimal_places=2,
                                 null=True,
                                 blank=True,
                                 default=0)
    savings = models.DecimalField(max_digits=30,
                                  decimal_places=2,
                                  null=True,
                                  blank=True,
                                  default=0)
    created_date = models.DateTimeField(auto_now_add=True,
                                        blank=True,
                                        null=True)
    modified_date = models.DateTimeField(auto_now=True,
                                         blank=True,
                                         null=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
