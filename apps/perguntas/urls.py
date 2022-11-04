from django.urls import path
from perguntas.views import *

urlpatterns = [
    path('', index, name='index' ),
    path( 'perguntas/', perguntas, name='perguntas'),
]