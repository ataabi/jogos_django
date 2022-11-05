from django.contrib import admin
from .models import Ranking

# Register your models here.

class ListandoUsuarios(admin.ModelAdmin):
    list_display = ('user','pontos_pergunta','pontos_forca')
    list_display_link = ('user',)
    search_fields = ('user',)
    ordering = ('pontos_pergunta','pontos_forca')
    
admin.site.register(Ranking, ListandoUsuarios)
