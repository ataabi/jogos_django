from django.urls import path
from .views import forca

urlpatterns = [
    path('forca', forca, name='forca' )
]