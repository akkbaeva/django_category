from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# Create your models here.
from category.models import Comment


class Users(AbstractUser):
    age = models.IntegerField()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

    def __str__(self):
        return f'{self.username}'
