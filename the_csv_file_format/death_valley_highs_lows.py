import os
import platform
import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Obtém as datas e as temperaturas máximas e mínimas do arquivo.
path = os.path.abspath(os.path.dirname(__file__))
if platform.system() == 'Linux':
    path += '/data/death_valley_2018_simple.csv'
else:
    path += '\\data\\death_valley_2018_simple.csv'

with open(path) as f:
    reader = csv.reader(f) # Passamos o objeto arquivo (f) como argumento a fim de criar um objeto reader
    # associado a esse arquivo.
    header_row = next(reader) # A função next() devolve a próxima linha do arquivo quando recebe 
    # o objeto reader.

    dates, highs, lows = [], [], [] # Lista para armazenar as datas e temperaturas máximas e mínimas em cada dia do arquivo.
    for row in reader: # Percorrendo as linhas anteriores do arquivo.
        ''' Sempre que analisamos uma linha, tentamos extrair a data e as temperaturas máximas e mínima.
            Se houver algum dado faltando, Python levantará um ValueError e o trataremos exibindo uma menssagem 
            de errro que inclua a data do dado ausente. '''
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d") # converte as informações de datas em um objeto datetime.
            high = int(row[4]) # Converte de string para inteiro.
            low = int(row[5]) # Converte de string para inteiro.
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date) # Concatenamos.
            highs.append(high) # Concatenamos.
            lows.append(low) # Concatenamos.

# Faz a plotagem dos dados.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c = 'red', alpha = 0.5) # O argumento alpha controla a transparência de uma cor.
ax.plot(dates, lows, c = 'blue', alpha = 0.5) # 0 é totalmente transparente e 1 é opaco.
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)
''' Para fill_between() passamos a lista dates para os valores de x e então as duas séries 
    com valores de y, highs e lows. O argumento facecolor determina a cor da região sombreada. '''

# Formatar o gráfico.
plt.title('Daily high and low temperatures - 2018\nDeath Valley, CA', fontsize = 20)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate() # Desenha os rótulos com as datas na diagonal para evitar que se sobreponha.
plt.ylabel('Temperature (F)', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()
