from django.contrib import admin
from .models import Palavra

# Register your models here.

class ListandoPalavras(admin.ModelAdmin):
    list_display = ('id','palavra')
    list_display_link = ('id','palavra')
    search_fields = ('palavra',)
    
admin.site.register(Palavra, ListandoPalavras)
