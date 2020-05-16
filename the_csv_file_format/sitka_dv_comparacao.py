import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from obter_dados_csv import obter_datas_temperaturas


# Nome dos arquivos.
filename_1 = 'death_valley_2014.csv'
filename_2 = 'sitka_weather_2014.csv'

# Obtém os dados de ambos os arquivos.
dados_1 = obter_datas_temperaturas(filename_1)
dados_2 = obter_datas_temperaturas(filename_2)

# Obtém as datas, temperaturas mínimas e máximas para Death Valley.
datas_1 = dados_1[0]
minimas_1 = dados_1[1]
maximas_1 = dados_1[2]

# Obtém as datas, temperaturas mínimas e máximas para Sitka.
datas_2 = dados_2[0]
minimas_2 = dados_2[1]
maximas_2 = dados_2[2]

# Faz a plotagem dos dados.
fig = plt.figure(dpi=128, figsize=(10, 6))

# Formata xaxis com 1 mês de intervalo e o formato da data.
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

# Plota o gráfico para o ano de 2014, Death Valley.
plt.plot(datas_1, maximas_1, c='red', alpha=0.3)
plt.plot(datas_1, minimas_1, c='blue', alpha=0.3)
plt.fill_between(datas_1, maximas_1, minimas_1, facecolor='blue', alpha=0.05)

# Plota o gráfico para o ano de 2014, Sitka.
plt.plot(datas_2, maximas_2, c='red', alpha=0.6)
plt.plot(datas_2, minimas_2, c='blue', alpha=0.6)
plt.fill_between(datas_2, maximas_2, minimas_2, facecolor='blue', alpha=0.15)

# Formata o gráfico.
title = 'Daily high and low temperatures - 2014'
title += '\nDeath Valley, CA and Sitka, AK'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.ylim(10, 120)

plt.show()
