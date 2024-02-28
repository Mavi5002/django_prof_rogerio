from django.db import models



DIVISAO_CHOICES=(
    ('A','SERIE A'),
    ('B','SERIE B'),
    ('C','SERIE C'),
    ('D','SERIE D')
)

SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Ferminino'),
)


class Time(models.Model):
    nome = models.CharField(max_length=100)
    
    ano_fundaçao = models.PositiveIntegerField(default=False)
    
    divisao_atual = models.CharField(choices=DIVISAO_CHOICES,max_length=120,null=True)
    
    image = models.ImageField(upload_to='imagem',null=True)
    
    sexo = models.CharField(choices=SEXO_CHOICES, max_length=32,null =True)
    


    def __str__(self):
        return self.nome







