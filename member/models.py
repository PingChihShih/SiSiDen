from django.db import models

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)

class Member(AbstractBaseUser, PermissionsMixin):
    table_id = models.IntegerField()

    USER_TYPE_CHOICES = (
        ("normal", "Normal"),
        ("admin", "Admin"),
    )

# Create your models here.
