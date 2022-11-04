from django.contrib import admin
from .models import Pergunta, RankingPergunta

# Register your models here.

class ListandoPerguntas(admin.ModelAdmin):
    list_display = ('id','pergunta')
    list_display_link = ('id','pergunta')
    search_fields = ('pergunta',)
    
admin.site.register(Pergunta, ListandoPerguntas)

class ListandoRankings(admin.ModelAdmin):
    list_display = ('user','pontos_pergunta')
    list_display_link = ('user','pontos_pergunta')
    search_fields = ('user',)
    
admin.site.register(RankingPergunta, ListandoRankings)
