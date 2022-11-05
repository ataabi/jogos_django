from django.db import models

# Create your models here.

class Palavra(models.Model):
    palavra = models.CharField(max_length=50)
    dica1 = models.CharField(max_length=150)
