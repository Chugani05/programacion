# *************************
# PRIMER ELEMENTO DUPLICADO
# *************************


def run(numbers: list) -> int:
    fdup = set()
    if number in numbers:
        if number in fdup:
            fdup = int(number)
        fdup.add(number)
    else:
        fdup = -1

    return fdup


if __name__ == '__main__':
    run([2, 3, 5, 3, 2])
