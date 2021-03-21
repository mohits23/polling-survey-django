# Generated by Django 3.1.1 on 2021-01-03 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_title', models.CharField(max_length=200, null=True)),
                ('question', models.CharField(max_length=150, null=True)),
                ('image', models.ImageField(null=True, upload_to='quiz_images')),
                ('text_response', models.CharField(max_length=300, null=True)),
                ('option_one', models.CharField(max_length=30, null=True)),
                ('option_two', models.CharField(max_length=30, null=True)),
                ('option_three', models.CharField(max_length=30, null=True)),
                ('option_four', models.CharField(max_length=30, null=True)),
                ('option_five', models.CharField(max_length=30, null=True)),
                ('option_six', models.CharField(max_length=30, null=True)),
                ('option_one_count', models.PositiveIntegerField(default=0)),
                ('option_two_count', models.PositiveIntegerField(default=0)),
                ('option_three_count', models.PositiveIntegerField(default=0)),
                ('option_four_count', models.PositiveIntegerField(default=0)),
                ('option_five_count', models.PositiveIntegerField(default=0)),
                ('option_six_count', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'quiz_table_temp',
            },
        ),
    ]