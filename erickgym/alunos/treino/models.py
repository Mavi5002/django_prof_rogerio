from django.db import models

class Exercicio(models.Model):
    nome = models.CharField(max_length=250)
    descricao = models.CharField(max_length=250)
    ativo = models.BooleanField(default=True)


# Create your models here.
