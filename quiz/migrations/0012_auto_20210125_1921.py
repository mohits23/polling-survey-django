# Generated by Django 3.1.1 on 2021-01-25 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_auto_20210125_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizmodel',
            name='correct_option_1',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='quizmodel',
            name='correct_option_2',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='quizmodel',
            name='correct_option_3',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='quizmodel',
            name='correct_option_4',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='quizmodel',
            name='correct_option_5',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='quizmodel',
            name='correct_option_6',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
