# Generated by Django 4.0.3 on 2022-03-19 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompetencyLevel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(default='Not specified')),
            ],
        ),
        migrations.CreateModel(
            name='Competency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='Not specified')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competencies', to='competitions.competencylevel')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='competencies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
