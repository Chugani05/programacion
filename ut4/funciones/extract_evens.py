# *******************
# EXTRACCIÓN DE PARES
# *******************


def is_even(value):
    return value % 2 == 0


def run(values: list) -> list:
    evens = []
    for value in values:
        if is_even(value):
            evens.append(value)
    return evens
