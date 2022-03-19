# Generated by Django 4.0.3 on 2022-03-19 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0002_alter_competencylevel_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SkillToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('tags', models.ManyToManyField(to='competitions.skilltag')),
            ],
        ),
        migrations.AddField(
            model_name='competency',
            name='skilltoken',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='competencies', to='competitions.skilltoken'),
        ),
    ]