from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length=10, null=False, blank=False)
    doctor_designation = models.CharField(max_length=20, null=True, blank=True)
    location = models.CharField(max_length=10, null=True, blank=True)
    timeslot = models.CharField(max_length=10, null=True, blank=True)
    doctor_exp = models.CharField(max_length=10, null=True, blank=True)
    doctor_image = models.ImageField(upload_to='media/', null=True, blank=True)
    role = models.CharField(max_length=10, null=True, blank=True)
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)
