# *********************
# ENCONTRANDO ISOGRAMAS
# *********************


def run(text: str) -> bool:
    ALPHABET = 'abcdefghijklmnñopqrstuvwxyz'
    letter_find = []
    text = text.lower()

    is_isogram = True

    for letters in text:
        if letters in ALPHABET:
            if letters not in letter_find:
                letter_find.append(letters)
                break
        else:
            is_isogram = False

    return is_isogram


if __name__ == '__main__':
    run('lumberjacks')
