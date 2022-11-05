from django.urls import path
from perguntas.views import *

urlpatterns = [
    path( 'perguntas/', perguntas, name='perguntas'),
]