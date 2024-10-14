# Projeto Django - Integração com OMDb API e Customização do Django Admin

## Descrição Geral

Este projeto é uma aplicação Django que faz o carregamento de uma planilha de diretores de filmes e enriquece os dados com informações obtidas da OMDb API. Além disso, a interface do Django Admin foi customizada para exibir informações detalhadas dos diretores e seus filmes.

## Pré-requisitos

- **Python 3.x**
- **Django 3.x ou superior**
- **Pandas**
- **aiohttp**
- **OMDb API Key** (requer cadastro gratuito no [site oficial do OMDb API](http://www.omdbapi.com/))

### Instalação das Dependências

1. Após clonar o repositório, navegue até a pasta do projeto:

   git clone https://github.com/seu_usuario/seu_projeto.git
   cd seu_projeto

2. Crie e ative um ambiente virtual:   

   python -m venv venv
   source venv/bin/activate  # No Windows use venv\Scripts\activate

3. Instale as dependências do projeto:

   ```pip install -r requirements.txt```
   
### Configuração do Projeto

1. Configuração da Chave da API OMDb

Para configurar a chave da API OMDb, crie um arquivo .env na raiz do projeto (onde estão o manage.py e outros arquivos principais do projeto). Adicione a seguinte linha ao arquivo .env:

  ```OMDB_API_KEY = 'sua_chave_omdb_api'```

O arquivo load_data.py já está configurado para carregar a chave da API do arquivo .env, então você não precisará modificar o código diretamente.

2. Utilização do Banco de Dados:

O repositório já contém o banco de dados SQLite pré-configurado, então não é necessário rodar migrações neste projeto.
O banco de dados está localizado no diretório principal do projeto, e já contém dados que podem ser utilizados diretamente no Django Admin.



## Uso

1. Inicie o servidor de desenvolvimento:

 ``` python manage.py runserver```

2. Acesse o Django Admin:

No navegador, vá até o seguinte endereço:

  http://127.0.0.1:8000/admin/

Faça login com as credenciais fornecidas ou crie um superusuário com o seguinte comando:

Para criar execute:

 ``` python manage.py createsuperuser```

  credencial para teste:

  usuário: admin
  senha: Lenix#edu1
  
3. Admin Customizado:

No Django Admin, você verá a interface customizada para gerenciar diretores de filmes e visualizar os dados enriquecidos pela OMDb API.

## Estrutura do Projeto

  - load_data.py: Comando Django personalizado para carregar dados de diretores a partir de uma planilha e enriquecê-los usando a OMDb API.
  - admin.py:  Arquivo responsável por configurar a interface do Django Admin para gerenciar os modelos do projeto. Ele permite registrar modelos para que estejam disponíveis na interface administrativa e             personalizar como esses modelos e seus campos são exibidos .
  - admin_site.py: Contém as customizações da interface do Django Admin para gerenciar diretores e exibir dados de filmes.
  - models.py:  Este arquivo define mos modelos Movie e Director, que representam, respectivamente, os modelos de filmes e diretores na aplicação.


Links Úteis:
- [Django Documentation](https://docs.djangoproject.com/)
- [OMDb API Documentation](http://www.omdbapi.com/)
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)

