from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django import forms
    

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password = None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user



class CustomUser(AbstractBaseUser):
    email = models.EmailField(blank = False, null = False, unique = True)
    password = models.CharField(max_length = 128)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
    
    

# Create your models here

