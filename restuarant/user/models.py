from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # Add any additional fields you need

    class Meta:
        # Specify unique related names for the groups and user_permissions fields
        # to avoid clashes with the built-in User model
        permissions = (
            ('group_permissions', 'Group permissions'),
            ('user_permissions', 'User permissions'),
        )

