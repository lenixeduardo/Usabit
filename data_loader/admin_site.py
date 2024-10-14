
from django.contrib.admin import AdminSite
from django.urls import path
from django.shortcuts import render
from .models import Director  

class MyCustomAdminSite(AdminSite):
    site_header = 'Admin Customizado'

    # Adicionando a view customizada que exibe diretores
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('directors/', self.admin_view(self.directors_list_view), name='directors_list'),
        ]
        return custom_urls + urls

    # View que exibe a lista de diretores
    def directors_list_view(self, request):
        directors = Director.objects.all()  # Pegando todos os diretores
        context = {
            'directors': directors
        }
        return render(request, 'admin/directors_list.html', context)

# Criando uma instância do Admin Customizado
my_admin_site = MyCustomAdminSite(name='myadmin')
