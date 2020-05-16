from pygal_maps_world.maps import World
wm = World() # Criamos uma instância da classe World().
wm.title = 'North, Central, and South America' # Definimos o atributo title() do mapa.

# usamos o método add() que aceita um rótulo e uma lista de códigos de países.
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

# O método render_to_file() cria um arquivo svg contendo o mapa, que poderá ser aberto no navegador.
wm.render_to_file('Americas.svg')
