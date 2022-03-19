from django.db import models

from user_auth.models import Profile


class CompetencyLevel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(default='Not specified', unique=True)


class SkillTag(models.Model):
    name = models.TextField(unique=True)


class SkillToken(models.Model):
    name = models.TextField()
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='skilltokens',
        null=True
    )
    tags = models.ManyToManyField(
        SkillTag,
        null=True,
        blank=True,
        related_name='tags')


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
    skilltoken = models.ForeignKey(
        SkillToken,
        null=True,
        on_delete=models.CASCADE,
        related_name='competencies')
