from django.db import models

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)

class Member(AbstractBaseUser):
    table_id = models.IntegerField()


# Create your models here.
