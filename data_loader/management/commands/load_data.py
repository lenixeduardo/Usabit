import pandas as pd
import aiohttp
import asyncio
from django.core.management.base import BaseCommand
from data_loader.models import Movie

OMDB_API_URL = 'http://www.omdbapi.com/'
OMDB_API_KEY = 'fece4a6f'  

class Command(BaseCommand):
    help = 'Carrega dados de filmes de uma planilha, enriquece-os com a API OMDb e salva no banco de dados'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Caminho para a planilha CSV ou Excel')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        # Carregar planilha usando pandas
        if file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            data = pd.read_excel(file_path)
        else:
            self.stderr.write("Formato de arquivo não suportado. Use CSV ou Excel.")
            return

        # Limpar e transformar os dados
        data.fillna('', inplace=True)  # Exemplo de limpeza de dados
        self.stdout.write(f"Carregando {len(data)} filmes da planilha.")

        # Fazer enriquecimento de dados via API OMDb
        enriched_data = asyncio.run(self.enrich_data(data))

        # Salvar os dados no banco de dados
        for movie in enriched_data:
            Movie.objects.create(
                title=movie['title'],
                year=movie['year'],
                genre=movie['genre'],
                imdb_rating=movie['imdb_rating'],
                plot=movie['plot']
            )
        self.stdout.write(f"{len(enriched_data)} filmes salvos no banco de dados.")

    async def enrich_data(self, data):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for _, row in data.iterrows():
                tasks.append(self.fetch_movie_data(session, row))
            enriched_data = await asyncio.gather(*tasks)
        return enriched_data

    async def fetch_movie_data(self, session, row):
        params = {
            't': row['title'],
            'y': row['year'],
            'apikey': OMDB_API_KEY
        }
        async with session.get(OMDB_API_URL, params=params) as response:
            if response.status == 200:
                movie_data = await response.json()
                return {
                    'title': row['title'],
                    'year': row['year'],
                    'genre': row['genre'],
                    'imdb_rating': movie_data.get('imdbRating', 'N/A'),
                    'plot': movie_data.get('Plot', 'N/A')
                }
            else:
                return {
                    'title': row['title'],
                    'year': row['year'],
                    'genre': row['genre'],
                    'imdb_rating': 'N/A',
                    'plot': 'N/A'
                }