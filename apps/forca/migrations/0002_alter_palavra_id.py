# Generated by Django 4.1.2 on 2022-11-04 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palavra',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]