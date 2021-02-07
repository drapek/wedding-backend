from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class UserTypes(models.TextChoices):
        ADMIN = 'admin'
        NEWLYWED = 'newlywed'  # is admin as well, but additionally this users it appears in some lists
        GUEST = 'guest'
        GUEST_ACCOMPANYING_PERSON = 'guest_accomp'

    user_type = models.CharField(max_length=32, choices=UserTypes.choices)
    is_vegan = models.BooleanField(default=False)
    is_attending = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.user_type in (self.UserTypes.ADMIN, self.UserTypes.NEWLYWED):
            self.is_staff = True
        return super().save(*args, **kwargs)
