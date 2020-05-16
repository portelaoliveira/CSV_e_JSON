import requests

# Faz uma chamada de API e armazena a resposta.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' # Armazenamos o URL da chamada da API.
r = requests.get(url) # Usamos requests para fazer a chamada.
print('Status Code:', r.status_code)
''' O objeto com a resposta tem um atributo chamado status_code, que nos informa se a resposta
    foi bem sucedida. '''

# Armazena a resposta da API em uma variável.
respose_dict = r.json()

# Processa o resultado.
print(respose_dict.keys())
