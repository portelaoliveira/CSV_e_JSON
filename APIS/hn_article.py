import requests
import json

# Faz uma chamada de API e armazene a resposta.
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explora a estrutura dos dados.
response_dict = r.json()
readable_file = 'data/hn_topstories.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)

''' Um argumento indent é usado para imprimir JSON de maneira bonita e torná-lo mais legível. 
    O padrão é . Para obter a representação JSON mais compacta, você deve usar para eliminar 
    o espaço em branco.(', ', ': ')(',', ':') '''