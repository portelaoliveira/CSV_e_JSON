import os
import platform
import json
from lib.country_codes import get_country_code
from pygal_maps_world.maps import World
from pygal.style import RotateStyle

path = os.path.abspath(os.path.dirname(__file__))
if platform.system() == 'Linux':
    path += '/data/gdp_json.json'
else:
    path += '\\data\\gdp_json.json'

# Carregar dados de uma lista.
with open(path) as f:
    gdp_data = json.load(f) # Armazenando os dados do objeto arquivo (f) na variável.
    # A função json.load() converte os dados em uma lista.

# Constrói um dicionário com dados das populações e os códigos dos países.
cc_gdps = {}
for gdp_dict in gdp_data: # Percorre cada item da lista.
    if gdp_dict["Year"] == 2016: # Procuramos 2010 na chave Year de cada dicionário.
        country_name = gdp_dict["Country Name"]
        gdp = int(float(gdp_dict["Value"])) # Armazenadas em um formato numérico.
        code_country = get_country_code(country_name)
        if code_country:
            cc_gdps[code_country] = gdp
            ''' O dicionário armazena o código do país como chave e a população
                como valor sempre que o código é devolvido. '''
# Agrupa os países em três níveis populacionais.
cc_gdps_1, cc_gdps_2, cc_gdps_3 = {}, {}, {}
for cc, gdp in cc_gdps.items():
    if gdp < 5000000000:
        cc_gdps_1[cc] = round(gdp / 1000000000)
    elif gdp < 50000000000:
        cc_gdps_2[cc] = round(gdp / 1000000000)
    else:
        cc_gdps_3[cc] = round(gdp / 1000000000)

# Vê quantos píses estão em cada nível.
print(len(cc_gdps_1), len(cc_gdps_2), len(cc_gdps_3))
wm_style = RotateStyle('#336699')
wm = World(style = wm_style) # Criamos uma instância da classe World().
wm.title = 'Global GDP in 2016, by Country (in billions USD)' # Definimos o atributo title() do mapa.
# usamos o método add() que aceita um rótulo (primiro argumento) e um dicionário de códigos de países (segundo argumento).
wm.add('0-5bn', cc_gdps_1)
wm.add('5bn-50bn', cc_gdps_2)
wm.add('>50bn', cc_gdps_3)

# O método render_to_file() cria um arquivo svg contendo o mapa, que poderá ser aberto no navegador.
wm.render_to_file('Global_gdp.svg')
