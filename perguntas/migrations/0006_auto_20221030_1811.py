# Generated by Django 3.1.3 on 2022-10-30 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perguntas', '0005_pergunta_alternativa1_pergunta_alternativa2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pergunta',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
