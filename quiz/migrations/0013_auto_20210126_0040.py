# Generated by Django 3.1.1 on 2021-01-25 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0012_auto_20210125_1921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizmodel',
            old_name='correct_option_1',
            new_name='correct_option',
        ),
        migrations.RemoveField(
            model_name='quizmodel',
            name='correct_option_2',
        ),
        migrations.RemoveField(
            model_name='quizmodel',
            name='correct_option_3',
        ),
        migrations.RemoveField(
            model_name='quizmodel',
            name='correct_option_4',
        ),
        migrations.RemoveField(
            model_name='quizmodel',
            name='correct_option_5',
        ),
        migrations.RemoveField(
            model_name='quizmodel',
            name='correct_option_6',
        ),
    ]
