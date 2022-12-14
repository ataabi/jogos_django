# Generated by Django 4.1.2 on 2022-11-05 02:10

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=django.contrib.auth.models.User, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('pontos_pergunta', models.IntegerField(default=0)),
                ('pontos_forca', models.IntegerField(default=0)),
            ],
        ),
    ]
