# Generated by Django 4.1.2 on 2022-10-29 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perguntas', '0003_remove_pergunta_alternativas_alternativas'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Alternativas',
            new_name='Alternativa',
        ),
    ]
