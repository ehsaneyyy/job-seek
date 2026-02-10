from django.db import models
from django.contrib.auth.models import AbstractUser
from user.manager import UserManager



# Create your models here.
class User(AbstractUser):
    username=None
    email=models.EmailField(unique=True,max_length=100,error_messages={"unique":"Email already Exists!"})
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

class Meta:
    db_table = "user_user"
    verbose_name = "User"
    verbose_name_plural = "Users"
    ordering = ["-id"]

    def __str__(self):
        return self.email
        


