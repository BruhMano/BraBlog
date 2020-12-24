from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to="media", blank = True, null = True)
    desc = models.TextField(default="BRUH", max_length=30)
    
