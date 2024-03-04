from django.contrib import admin
from core.models import Time,Jogador,Competiçao,TitulodasCompetições
from django.utils.html import format_html


@admin.register(TitulodasCompetições)
class TitulodasCompetiçõesAdmin(admin.ModelAdmin):
    list_display=['time','ano','resultado',]


@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display=['image_tag','nome','ano_fundaçao','divisao_atual','sexo','pais','uf','cidade']

    def image_tag(self,time):
        return format_html(f'<img src="{time.image.url}" width="60" />')
    
@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ['image_tag','nome','time','num_camisa','sexo']
    
    def image_tag(self,jogador):
        return format_html(f'<img src="{jogador.image.url}" width="60" />')

@admin.register(Competiçao)
class CompetiçaoAdmin(admin.ModelAdmin):
    list_display =['nome','Tipo_da_competição']


# Register your models here.
