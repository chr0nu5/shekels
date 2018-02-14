from .models import User
from django.contrib import admin
from django.contrib.auth.models import User as DjangoUser

# Remove default models here.
admin.site.unregister(DjangoUser)

# Register your models here.
admin.site.register(User)
