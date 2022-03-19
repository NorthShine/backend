from django.db import models


class CompetencyLevel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(default='Not specified')


class Competency(models.Model):
    name = models.TextField(default='Not specified')
    level = models.ForeignKey(CompetencyLevel, on_delete=models.CASCADE)
