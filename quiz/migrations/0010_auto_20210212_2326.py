# Generated by Django 3.1.6 on 2021-02-12 23:26

from django.db import migrations, models
import quiz.models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_auto_20210211_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='playId',
            field=models.CharField(default=quiz.models.key_generator, editable=False, max_length=7),
        ),
    ]
