# *******************
# CONSONANTES COMUNES
# *******************


def run(text1: str, text2: str) -> str:
    cconst = text1.lower & text2.lower

    return cconst


if __name__ == '__main__':
    run('Flat is bEtter than nested', 'Readability counts')
