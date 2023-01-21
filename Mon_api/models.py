from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class ApiModel(models.Model):
    url = models.URLField(
        max_length=100,
        blank=False,
        null=True,
    )