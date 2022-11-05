from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ranking(models.Model):
    user = models.OneToOneField(User, primary_key=User, related_name='Ranking' ,  on_delete=models.CASCADE)
    pontos_pergunta = models.IntegerField(default=0)
    pontos_forca = models.IntegerField(default=0)
    pontos_rpg = models.IntegerField(default=0)