from django.db import models

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)


class Member(AbstractBaseUser, PermissionsMixin):
    """
    total_point: This is the point which is consumed for growing a tree.
    app_point: This is the basic point of this app.
    """
    table_id = models.IntegerField()


# Create your models here.
