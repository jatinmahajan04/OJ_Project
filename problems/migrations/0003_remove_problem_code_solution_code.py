# Generated by Django 4.2.13 on 2024-06-03 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_alter_problem_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='code',
        ),
        migrations.AddField(
            model_name='solution',
            name='code',
            field=models.TextField(blank=True),
        ),
    ]