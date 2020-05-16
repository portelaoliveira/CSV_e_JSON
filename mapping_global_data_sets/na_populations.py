from pygal_maps_world.maps import World
wm = World() # Criamos uma instância da classe World().
wm.title = 'Populations of Countries in North America' # Definimos o atributo title() do mapa.

# usamos o método add() que aceita um rótulo (primiro argumento) e um dicionário de códigos de países (segundo argumento).
wm.add('North America ', {'ca':34126000, 'us':309349000, 'mx':113423000})

# O método render_to_file() cria um arquivo svg contendo o mapa, que poderá ser aberto no navegador.
wm.render_to_file('na_populations.svg')

