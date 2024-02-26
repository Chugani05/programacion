# *************************
# SIMULANDO EL COMANDO TAIL
# *************************
from pathlib import Path


def run(file: Path, n: int) -> str:
    with open(file, 'r') as f:
        line = f.readlines()
        lines = ''.join(line[-n:]).rstrip('\n')

    return lines


if __name__ == '__main__':
    run('data/tail/nba_season22.txt', 3)
