from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

DEPARTMENT_CHOICES = [
    ("CYBER AND TECHNICAL DEPARTMENT", 'CTD'),
    ("HEADQUARTERS", 'HQ'),
    ("EVALUATION ANALYSIS AND PRODUCTION", 'EAP'),
    ("COUNTER TERRORISM", 'CT'),
  
]

class CustomUser(AbstractUser):
    USERNAME_FIELD = 'username'
    department = models.CharField(choices = DEPARTMENT_CHOICES, max_length=255, blank=True)
    role = models.CharField(max_length=30, blank=True)
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
