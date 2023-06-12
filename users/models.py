from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.managers import AppUserManager


class AppUser(AbstractUser):
    email = models.EmailField(_('email'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = AppUserManager()

    def __str__(self):
        return self.email
