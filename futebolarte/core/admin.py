from django.contrib import admin
from core.models import Time

@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):

    list_display = ['nome','estado','cores','ano_fundaçao','tem_mundial']
    list_filter = ['tem_mundial']
    search_fields = ['estado','cores'] 


# Register your models here.
