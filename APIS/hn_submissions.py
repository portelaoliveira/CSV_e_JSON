import requests
from operator import itemgetter

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
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}", # Link para página de discurssão desse item.
        'comments': response_dict['descendants'], # Número de comentários no dicionário.
        }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key = itemgetter('comments'), reverse = True)
''' A função itemgetter('comments') ordena a lita de dicionário de acordo com o número de comentários. 
    A função sorted() então utiliza esse valor como base para ordenar a lista. Ordenamos a lista na 
        ordem inversa para colocar as histórias mais comentadas antes. '''

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

