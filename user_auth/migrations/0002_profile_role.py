# Generated by Django 4.0.3 on 2022-03-19 08:18

from django.db import migrations, models

from user_auth.models import Profile


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('EMPLOYEE', 'employee'), ('EMPLOYER', 'employer')], default='EMPLOYEE', max_length=10),
        ),
    ]