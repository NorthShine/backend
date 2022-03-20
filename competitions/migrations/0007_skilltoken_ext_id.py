# Generated by Django 4.0.3 on 2022-03-20 05:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0006_alter_skilltoken_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='skilltoken',
            name='ext_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
