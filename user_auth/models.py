from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    EMPLOYER = 'EMPLOYER'
    EMPLOYEE = 'EMPLOYEE'

    ROLES = [
        ('EMPLOYEE', 'employee'),
        ('EMPLOYER', 'employer')
    ]
    name = models.TextField(blank=True, null=True)
    role = models.CharField(
        max_length=10, choices=ROLES,
        default=EMPLOYEE)
    email = models.EmailField(unique=True)
