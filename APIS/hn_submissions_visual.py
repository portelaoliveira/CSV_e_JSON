import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Faz uma chamada de API e armazena a resposta.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
''' Essa chamada de API devolve uma lista contendo os IDs dos 500 artigos mais populares do Hacker News 
    no momento em que a chamada é feita. '''
r = requests.get(url)
print('Status code:', r.status_code)

# Processa informações sobre cada artigo submetido.
submission_ids = r.json() # Covertemos o texto em uma lista Python.
submission_dicts = [] # Usaremos esse IDs para criar um conjunto de diconários em que cada um aramzena informaçôes sobre um dos artigos submetidos.
for submission_id in submission_ids[:10]: # Percorre os IDs dos 10 principais artigos submetidos.
    # Cria uma chamada de API separada para cada artigo submetido.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json" # Faz uma nova chamada de API para cada artigo gerando um URL que inclui o valor atual.
    submission_r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {submission_r.status_code}") # Ver se foi bem sucedido
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'], # Título do artigo.
        'link': f"http://news.ycombinator.com/item?id={submission_id}", # Link para página de discurssão desse item.
        'comments': response_dict.get('descendants', 0), # Número de comentários no dicionário.
        }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, 
                        key = itemgetter('comments'), 
                        reverse = True)
''' A função itemgetter('comments') ordena a lita de dicionário de acordo com o número de comentários. 
    A função sorted() então utiliza esse valor como base para ordenar a lista. Ordenamos a lista na 
        ordem inversa para colocar as histórias mais comentadas antes. '''

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['link']}")
    print(f"Comments: {submission_dict['comments']}")

titles, plot_dicts = [], []
for submission_dict in submission_dicts:
    titles.append(submission_dict['title'])

    plot_dict = {
        'value': submission_dict['comments'],
        'label': submission_dict['title'],
        'xlink': submission_dict['link'], # O pygal usa o URL associado a 'xlink' para transformar cada barra em um link ativo.
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
my_config.y_title = 'Number of Comments'

chart = pygal.Bar(my_config, style = my_style) # O método Bar() cria um gráfico de barras.
chart.title = 'Most-Active Discussions on Hacker News' 
chart.x_labels = titles

chart.add('', plot_dicts)
chart.render_to_file('hn_submission_visual.svg')
