import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Faz uma chamada de API e armazena a resposta.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' # Armazenamos o URL da chamada da API.
r = requests.get(url) # Usamos requests para fazer a chamada.
print('Status Code:', r.status_code)
''' O objeto com a resposta tem um atributo chamado status_code, que nos informa se a resposta
    foi bem sucedida. '''

# Armazena a resposta da API em uma variável.
respose_dict = r.json()
print('Total repositories:', respose_dict['total_count']) # Total de repositórios python no GitHub.

# Explora informaçôes sobre os repositórios.
repo_dicts = respose_dict['items']
print('Repositories returned:', len(repo_dicts))

names, plot_dicts = [], []
''' As listas vazias vão armazenar o nome de cada projeto para rotular as barras e o número de estrelas
    para determinar a altura delas. '''
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'], # O pygal usa o URL associado a 'xlink' para transformar cada barra em um link ativo.
        }
    plot_dicts.append(plot_dict)

# Cria a vizualização.
my_style = LS('#333366', base_style = LCS)

my_config = pygal.Config() # Cria uma instância da classse Config().
my_config.x_label_rotation = 45 # x_label_rotation = 45 define a rotação dos nomes ao longo do eixo X.
my_config.show_legend = False # Não mostra as legendas.
my_config.title_font_size = 24 # Definimos o tamaho da fonte para o título do gráfico.
my_config.label_font_size = 14 # Definimos o tamaho da fonte para o rótulos menor (nomes dos projetos ao longo do eixox).
my_config.major_label_font_size = 18 # Definimos o tamaho da fonte para o rótulos maior (número no eixo y).
my_config.truncate_label = 15 # Reduz os nomes dos projetos mais longos a 15 caracteres.
my_config.show_y_guides = False # Oculta as linhas horizontais do gráfico.
my_config.width = 1000 # Definimos uma largura personalizada para que o gráfico use mais do espaço disponível no navegador.

chart = pygal.Bar(my_config, style = my_style) # O método Bar() cria um gráfico de barras.
chart.title = 'Most-Starred Python Projects on GitHub' 
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('Bar_python_repos_visual.svg')
