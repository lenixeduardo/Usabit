from django.contrib import admin
from .models import Movie, Director

# Personalizando a exibição do modelo no admin
class MovieAdmin(admin.ModelAdmin):
    # Exibindo colunas: combinação de título e ano, gênero e classificação do IMDb
    list_display = ('movie_details', 'genre', 'imdb_rating')

    # Filtros para facilitar a navegação
    list_filter = ('genre', 'year')

    # Campos de busca
    search_fields = ('title', 'genre')

    # Permite edição direta de classificações IMDb na lista de filmes
    list_editable = ('imdb_rating',)

    # Ordena por ano, do mais recente para o mais antigo
    ordering = ('-year',)

    # Função que combina o título e o ano do filme em uma só coluna
    def movie_details(self, obj):
        return f"{obj.title} ({obj.year})"
    
    # Definindo o título da coluna personalizada
    movie_details.short_description = 'Filme (Ano)'

# Registrando o modelo com as personalizações
admin.site.register(Movie, MovieAdmin)


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate', 'nationality')

admin.site.register(Director, DirectorAdmin)
