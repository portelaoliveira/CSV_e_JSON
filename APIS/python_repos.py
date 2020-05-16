import requests

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

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}") # Nome do projeto.
    print(f"Owner: {repo_dict['owner']['login']}") # Acessa o dicionário que o representa com owner e então usamos a chave login para obter o seu nome de login.
    print(f"Stars: {repo_dict['stargazers_count']}") # Exibe a quantidade de estrelas que o projeto recebeu.
    print(f"Repository: {repo_dict['html_url']}") # Extraí o URL do repositório no GitHub.
    print(f"Created: {repo_dict['created_at']}") # Mostra a data em que o projeto foi criado.
    print(f"Updated: {repo_dict['updated_at']}") # Quando foi atualizado pela última vez.
    print(f"Description: {repo_dict['description']}") # Exibe a descrição do repositório.

