# Generated by Django 4.1 on 2022-08-13 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_attempquiz_right_ans'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempquiz',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.quiz'),
        ),
    ]
