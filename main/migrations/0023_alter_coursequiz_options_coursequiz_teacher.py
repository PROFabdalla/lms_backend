# Generated by Django 4.1 on 2022-08-12 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_quiz_quizquestions_coursequiz'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursequiz',
            options={'verbose_name_plural': 'courses Quiz'},
        ),
        migrations.AddField(
            model_name='coursequiz',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.teacher'),
        ),
    ]
