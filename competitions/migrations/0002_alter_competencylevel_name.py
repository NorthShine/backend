# Generated by Django 4.0.3 on 2022-03-19 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competencylevel',
            name='name',
            field=models.TextField(default='Not specified', unique=True),
        ),
    ]
