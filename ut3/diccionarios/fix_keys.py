# ********************
# LA CLAVE ES LA CLAVE
# ********************


def run(items: dict) -> dict:
    keys = list(items.keys())
    cleaning_keys = [key.strip() for key in keys]
    fitems = {cleaning_key: items[key] for cleaning_key, key in zip(cleaning_keys, keys)}

    # fitems = {key.strip(): value for key, value in items.items()}

    return fitems


if __name__ == '__main__':
    run({'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']})
