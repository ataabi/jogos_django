from django.urls import path
from usuarios.views import *

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout')
]
