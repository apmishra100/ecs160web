from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from simple_email_confirmation import SimpleEmailConfirmationUserMixin
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import BaseUserManager


# Create your models here.

'''class UserProfile(models.Model):
    user   = models.OneToOneField(User)
    picture = models.ImageField(upload_to="images")
    REQUIRED_FIELDS = ('user', 'email',)
    
    def __unicode__(self):
        return self.user.usernam'''

class CustomUserManager(BaseUserManager):

    def create_user(self, userName, password=None, **extra_fields):
        userName = userName
        user = self.model(userName=userName, is_staff=False, is_active=True, is_superuser=False, is_admin = False)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, userName, password, **extra_fields):
        userName = userName
        user = self.model(userName=userName, is_staff=False, is_active=True, is_superuser=True, is_admin = True)
        user.set_password(password)
        user.save(using=self._db)
        return user
        


        
class User(SimpleEmailConfirmationUserMixin, AbstractBaseUser):
        userName = models.CharField(max_length=31, unique = True)
        picture =models.ImageField(upload_to="images")
        firstName = models.CharField(max_length=31)
        lastName = models.CharField(max_length=31)
        email = models.EmailField('email address')
        is_active = models.BooleanField(default = False)
        is_admin = models.BooleanField(default = False)
        is_online = models.BooleanField(default = False)
        
        USERNAME_FIELD = 'userName'
        REQUIRED_FIELDS = []
        
        objects = CustomUserManager()

        def __unicode__(self):
            return self.userName
        
        @property
        def is_superuser(self):
            return self.is_admin

        @property
        def is_staff(self):
            return self.is_admin

        def has_perm(self, perm, obj=None):
            return self.is_admin

        def has_module_perms(self, app_label):
            return self.is_admin
        
        def get_short_name(self):
            return self.userName
            
        def get_email(self):
            return self.email
