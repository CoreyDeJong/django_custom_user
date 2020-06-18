from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    # email = models.EmailField(('email address'), blank=True, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

def __str__(self):
    return self.username