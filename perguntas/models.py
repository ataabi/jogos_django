from django.db import models

# Create your models here.

class Pergunta(models.Model):
    pergunta = models.CharField(max_length=200)
    resposta = models.CharField(max_length=100)
    alternativa1 = models.CharField(max_length=100, blank=True) 
    alternativa2 = models.CharField(max_length=100, blank=True) 
    alternativa3 = models.CharField(max_length=100, blank=True) 
    alternativa4 = models.CharField(max_length=100, blank=True) 
    alternativa5 = models.CharField(max_length=100, blank=True) 

    def lista_alternativas(self):
        return [
            self.alternativa1,
            self.alternativa2,
            self.alternativa3,
            self.alternativa4,
            self.alternativa5
        ]

    def __str__(self):
        return self.pergunta
