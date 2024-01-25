'''Create your models here.'''
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """Company staffs and users"""
    email = models.EmailField(_('email address'), unique=True, blank=True, null=True)
    user_roles = (
        ('student', 'student'),
        ('staff', 'staff'),
        ('admin', 'admin'),
        ('editor', 'editor'),
    )
    role = models.CharField(_("role"), max_length=50, blank=True, null=True)
    nationality = models.CharField(_("nationality"), max_length=50, blank=True, null=True)
    mobile_number = models.CharField(_("mobile_number"), max_length=50, blank=True, null=True)
    country = models.CharField(_("country"), max_length=50, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return f"{self.username}"



