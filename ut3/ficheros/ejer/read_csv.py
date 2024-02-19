# ********************
# LEYENDO FICHEROS CSV
# ********************
from pathlib import Path


def run(datafile: Path) -> list:
    data = []
    with open(datafile) as f:
        lines = f.readlines()
        column_names = lines[0].strip().split(',')
        for line in lines[1:]:
            values = line.strip().split(',')
            diccionario = {}
            for clave, valor in zip(column_names, values):
                if valor.lower() == 'true':
                    diccionario[clave] = True
                elif valor.lower() == 'false':
                    diccionario[clave] = False
                elif valor.isdigit():
                    diccionario[clave] = int(valor)
                else:
                    diccionario[clave] = valor if valor != '' else None
            data.append(diccionario)
    return data


if __name__ == '__main__':
    run('data/read_csv/pokemon.csv')
