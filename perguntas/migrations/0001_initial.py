# Generated by Django 4.1.2 on 2022-10-16 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.CharField(max_length=200)),
                ('resposta', models.CharField(max_length=100)),
                ('alternativas', models.TextField()),
            ],
        ),
    ]
