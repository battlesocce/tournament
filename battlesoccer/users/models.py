from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_team = models.BooleanField(default=False)
    is_activated = models.BooleanField(default=False)


