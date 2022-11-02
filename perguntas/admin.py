from django.contrib import admin
from .models import Pergunta

# Register your models here.

class ListandoPerguntas(admin.ModelAdmin):
    list_display = ('id','pergunta')
    list_display_link = ('id','pergunta')
    search_fields = ('pergunta',)
    
admin.site.register(Pergunta, ListandoPerguntas)