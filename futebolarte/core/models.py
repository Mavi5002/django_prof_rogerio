from django.db import models


ESTADO_CHOICES = (
    ('AC','Acre'),
    ('RS','Rio Grande do Sul'),
    ('SP','São Paulo'),
    ('RJ','Rio de Janeiro')
)

class Time(models.Model):
    nome = models.CharField(max_length=120)
    estado = models.CharField(choices=ESTADO_CHOICES,max_length=120,null = True)
    cores = models.CharField(max_length=80,blank= True, null=True)
    ano_fundaçao = models.PositiveIntegerField(default=False)
    tem_mundial = models.BooleanField(default=False)


    def __str__(self):
        return self.nome
