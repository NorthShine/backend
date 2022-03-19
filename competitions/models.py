from django.db import models

from user_auth.models import Profile


class CompetencyLevel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(default='Not specified')


class Competency(models.Model):
    name = models.TextField(default='Not specified')
    level = models.ForeignKey(
        CompetencyLevel,
        on_delete=models.CASCADE,
        related_name='competencies')
    user = models.ForeignKey(
        Profile,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='competencies')
