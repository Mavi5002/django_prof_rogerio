from django.db import models

DIVISAO_CHOICES=(
    ('A','SÉRIE A'),
    ('B','SÉRIE B'),
    ('C','SÉRIE C'),
    ('D','SÉRIE D'),
)

SEXO_CHOICES =(
    ('F','FERMININO'),
    ('M','MASCULINO'),
)

COMPETIÇAO_CHOICES=(
    ('UF','Estadual'),
    ('NL','Nacional'),
    ('IN','Internacional'),
)

CATEGORIA_CHOICES=(
    ('CP','Copa'),
    ('CPN','Campeonato')
)

RESULTADO_CHOICES=(
    ('CP','Campeão'),
    ('VC','Vice-Campeão')
)



class Time(models.Model):
    image = models.ImageField(upload_to='imagem',null=True)
    nome = models.CharField(max_length=100)
    ano_fundaçao = models.PositiveIntegerField(default=False)
    divisao_atual = models.CharField(choices=DIVISAO_CHOICES,null=True,max_length=100)
    sexo = models.CharField(choices=SEXO_CHOICES,null=True,max_length=100)
    cidade = models.CharField(max_length=100,null=True)
    uf = models.CharField(max_length=120,null=True)
    pais = models.CharField(max_length=100,null=True)


    class Meta:
        verbose_name = 'Time'
        verbose_name_plural = 'Times'

    def __str__(self):
        return self.nome

class Jogador(models.Model):
    time = models.ForeignKey(Time,on_delete=models.CASCADE, related_name='jogador')
    image = models.ImageField(upload_to='imagem',null=True)
    nome = models.CharField(max_length=100)
    num_camisa = models.PositiveIntegerField(default=False)
    sexo = models.CharField(choices=SEXO_CHOICES,null=True,max_length=100)
   
    
    
    class Meta:
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'

class Competiçao(models.Model):
    nome = models.CharField(max_length=100)
    Tipo_da_competição= models.CharField(max_length=180,choices=COMPETIÇAO_CHOICES,null=True)
    categoria = models.CharField(max_length=32,choices=CATEGORIA_CHOICES,null=True)

    class Meta:
        verbose_name = 'Competição'
        verbose_name_plural = 'Competições'

class TitulodasCompetições(models.Model):
    time = models.ForeignKey(Time,on_delete=models.CASCADE,related_name='titulodoclube')
    ano = models.PositiveIntegerField(default=False)
    
    resultado = models.CharField(max_length=30,choices=RESULTADO_CHOICES,null=True)
    

    
    class Meta:
        verbose_name = 'Título'
        verbose_name_plural = 'Título'


  






    

# Create your models here.
