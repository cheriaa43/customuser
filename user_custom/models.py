from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    display_name = models.CharField(max_length=150)
    homepage = models.URLField(blank=True, null=True)
