from django.contrib import admin
from core.models import Time,Jogador

@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):

    list_display = ['nome','estado','cores','ano_fundaçao','tem_mundial']
    list_filter = ['tem_mundial']
    search_fields = ['estado','cores'] 

@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ['nome','clube','posiçao_principal']

# Register your models here.
