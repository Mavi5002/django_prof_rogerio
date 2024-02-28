from django.contrib import admin
from core.models import Time
from django.utils.html import format_html

@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ['image_tag','nome','ano_fundaçao','divisao_atual','sexo']
    

    def image_tag(self,time):
        return format_html(f'<img src="{time.image.url}" width="60" />')
    





# Register your models here.
