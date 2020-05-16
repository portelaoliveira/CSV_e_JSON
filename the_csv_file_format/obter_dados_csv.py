import csv
from datetime import datetime


def obter_datas_temperaturas(arquivo: str) -> str or tuple:
    """
    -> Obtém as datas, temperaturas mínimas e temperaturas máximas
    de um arquivo csv.

    :param arquivo: Nome do arquivo csv.
    :return: Retorna uma tupla com 3 listas:
    as datas, temperaturas máximas e mínimas.
    """

    try:
        with open(arquivo) as obj_arq:
            conteudo = csv.reader(obj_arq)
            # Pula a linha que contém os headers.
            next(conteudo)

            # Listas das datas, temp. máximas e mínimas.
            datas, maximas, minimas = [], [], []
            for linha in conteudo:
                try:
                    data_atual = datetime.strptime(linha[0], '%Y-%m-%d').date()

                    maxima = int(linha[1])
                    minima = int(linha[3])
                    if minima == 0:
                        minima = 50
                except ValueError:
                    print(data_atual, 'Faltando dados.')
                else:
                    datas.append(data_atual)
                    maximas.append(maxima)
                    minimas.append(minima)
    except FileNotFoundError:
        return f"O arquivo '{arquivo}' não existe."
    else:
        return datas, maximas, minimas


def obter_datas_indices_pluvio(arquivo: str) -> str or tuple:
    """
    -> Obtém as datas e o indices pluviométrico de um arquivo
    csv.

    :param arquivo: Nome do arquivo csv.
    :return: Retorna uma tupla com 2 listas:
    as datas e os indices pluviométricos.
    """

    try:
        with open(arquivo) as obj_arq:
            conteudo = csv.reader(obj_arq)
            # Pula a linha que contém os headers.
            next(conteudo)

            # Listas das datas e indices pluviometricos.
            datas, indices_pluvio = [], []
            for linha in conteudo:
                try:
                    data_atual = datetime.strptime(linha[0], '%Y-%m-%d').date()
                    indice_pluvio = float(linha[16])
                except ValueError:
                    print(data_atual, 'Faltando dados.')
                else:
                    datas.append(data_atual)
                    indices_pluvio.append(indice_pluvio)
    except FileNotFoundError:
        return f"O arquivo '{arquivo}' não existe."
    else:
        return datas, indices_pluvio


def obter_datas_umidades(arquivo: str) -> str or tuple:
    """
    -> Obtém as datas, umidade máximas e mínimas
    de um arquivo csv.

    :param arquivo: Nome do arquivo csv.
    :return: Retorna uma tupla com 3 listas:
    as datas, umidades máximas e mínimas.
    """
    try:
        with open(arquivo) as obj_arq:
            conteudo = csv.reader(obj_arq)
            # Pula a linha que contém os headers.
            next(conteudo)

            # Listas das datas, umidades máximas e mínimas.
            datas, umidades_maximas, umidades_minimas = [], [], []
            for linha in conteudo:
                try:
                    data_atual = datetime.strptime(linha[0], '%Y-%m-%d').date()

                    umidade_maxima = int(linha[7])
                    umidade_minima = int(linha[9])
                    if umidade_minima == 0:
                        umidade_minima = 55
                except ValueError:
                    print(data_atual, 'Faltando dados.')
                else:
                    datas.append(data_atual)
                    umidades_maximas.append(umidade_maxima)
                    umidades_minimas.append(umidade_minima)
    except FileNotFoundError:
        return f"O arquivo '{arquivo}' não existe."
    else:
        return datas, umidades_maximas, umidades_minimas
