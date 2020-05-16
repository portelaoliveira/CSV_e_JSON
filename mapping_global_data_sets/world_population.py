import os
import platform
import json
from lib.country_codes import get_country_code
from pygal_maps_world.maps import World
from pygal.style import RotateStyle

path = os.path.abspath(os.path.dirname(__file__))
if platform.system() == 'Linux':
    path += '/data/population_data_json.json'
else:
    path += '\\data\\population_data_json.json'

# Carregar dados de uma lista.
with open(path) as f:
    pop_data = json.load(f) # Armazenando os dados do objeto arquivo (f) na variável.
    # A função json.load() converte os dados em uma lista.

# Constrói um dicionário com dados das populações e os códigos dos países.
cc_populations = {}
for pop_dict in pop_data: # Percorre cada item da lista.
    if pop_dict["Year"] == 2010: # Procuramos 2010 na chave Year de cada dicionário.
        country_name = pop_dict["Country Name"]
        population = int(float(pop_dict["Value"])) # Armazenadas em um formato numérico.
        code_country = get_country_code(country_name)
        if code_country:
            cc_populations[code_country] = population
            ''' O dicionário armazena o código do país como chave e a população
                como valor sempre que o código é devolvido. '''

# Agrupa os países em três níveis populacionais.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# Vê quantos píses estão em cada nível.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))
wm_style = RotateStyle('#336699')
wm = World(style = wm_style) # Criamos uma instância da classe World().
wm.title = 'World Population in 2010, by country' # Definimos o atributo title() do mapa.
# usamos o método add() que aceita um rótulo (primiro argumento) e um dicionário de códigos de países (segundo argumento).
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

# O método render_to_file() cria um arquivo svg contendo o mapa, que poderá ser aberto no navegador.
wm.render_to_file('World_population.svg')

