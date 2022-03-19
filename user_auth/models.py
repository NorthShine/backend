from django.db import models
from django.contrib.auth.models import User


class Profile(User):
    EMPLOYER = 'EMPLOYER'
    EMPLOYEE = 'EMPLOYEE'

    ROLES = [
        ('EMPLOYEE', 'employee'),
        ('EMPLOYER', 'employer')
    ]
    role = models.CharField(
        max_length=10, choices=ROLES,
        default=EMPLOYEE)
