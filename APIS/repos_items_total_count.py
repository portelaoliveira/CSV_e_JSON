import requests

# Faz uma chamada de API e armazena a resposta.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' # Armazenamos o URL da chamada da API.
r = requests.get(url) # Usamos requests para fazer a chamada.
print('Status Code:', r.status_code)
''' O objeto com a resposta tem um atributo chamado status_code, que nos informa se a resposta
    foi bem sucedida. '''

# Armazena a resposta da API em uma variável.
respose_dict = r.json()
print('Total repositories:', respose_dict['total_count']) # Número total de repositórios Python no GitHub.

# Explora informações sobre os repositórios.
repo_dicts = respose_dict['items'] # 'items' é uma lista que contém vários dicionários, cada um contém dados sobre um repositório.
print('Repositories returned:', len(repo_dicts))

# Analisa o primeiro repositório.
repo_dict = repo_dicts[0] # Primeiro item.
print('\nKeys:', len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
