from django.contrib.auth.models import AbstractUser
from django.db import models

from phone_store_for_GITHUB import settings


class User(AbstractUser):
    image = models.ImageField(upload_to='media/profile_photo', verbose_name="Image", blank=True, null=True,
                              default=settings.DEFAULT_USER_PHOTO)
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='date of birth')
