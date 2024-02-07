# ****************
# CONTANDO COMO WC
# ****************
from pathlib import Path


def run(input_path: Path) -> tuple:
    # TU CÓDIGO AQUÍ
    num_lines = num_words = num_bytes = 'output'

    return num_lines, num_words, num_bytes


if __name__ == '__main__':
    run('data/wc/lorem.txt')