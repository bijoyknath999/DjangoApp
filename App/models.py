from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class namaz_time_table (models.Model):
    namaz_name = models.CharField(max_length=50)
    namaz_time = models.CharField(max_length=50)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=14)
    admin_access = models.BooleanField(default = False)
    is_verified = models.BooleanField(default=False)
    last_login_time = models.DateTimeField(null=True, blank=True)
    last_logout_time = models.DateTimeField(null=True, blank=True)

    objects = UserManager()
   
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []
    