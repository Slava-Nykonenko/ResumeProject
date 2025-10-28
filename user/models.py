from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=13, unique=True)
    github = models.URLField()
    linkedin = models.URLField()
    facebook = models.URLField()

    def __str__(self):
        return self.first_name + " " + self.last_name
