# data_loader/urls.py
from django.urls import path
from . import views  # Certifique-se de que o 'views.py' existe e está correto

# Definindo as URLs do app
urlpatterns = [
    path('sample/', views.sample_view, name='sample'),  # Exemplo de uma rota
]
