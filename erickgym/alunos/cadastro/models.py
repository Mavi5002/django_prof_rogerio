from django.db import models

SEXO_CHOICES =(
    ('F','FERMININO'),
    ('M','MASCULINO'),
)

class Aluno(models.Model):

    image = models.ImageField(null=True)
    nome = models.CharField(max_length=100)
    sexo = models.CharField(choices=SEXO_CHOICES,max_length=120)
    dt_nasc = models.PositiveIntegerField(default=False)
    tel = models.PositiveIntegerField(default=False)
    cpf = models.PositiveIntegerField(default=False)

