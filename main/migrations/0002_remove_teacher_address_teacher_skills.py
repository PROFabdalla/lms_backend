# Generated by Django 4.1 on 2022-08-04 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='address',
        ),
        migrations.AddField(
            model_name='teacher',
            name='skills',
            field=models.TextField(null=True),
        ),
    ]