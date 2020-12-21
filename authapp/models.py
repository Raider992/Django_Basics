from django.db import models
from django.contrib.auth.models import AbstractUser

import birthday

class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    birthday = birthday.fields.BirthdayField()
    age = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.username