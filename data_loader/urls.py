
from django.urls import path
from . import views 

# Definindo as URLs do app
urlpatterns = [
    path('sample/', views.sample_view, name='sample'),  
]
