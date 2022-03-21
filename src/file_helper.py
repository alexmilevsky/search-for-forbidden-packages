import os


# Базовая функция для поиска по всем папкам каталога
from csv import DictReader


def find_files(catalog, f):
    find_files = []
    for root, dirs, files in os.walk(catalog):
        find_files += [os.path.join(root, name) for name in files if name == f]
    return find_files


# Парсим список словарей из csv
def get_list_dictionaries_from_csv(file):
    with open(file, 'r') as read_obj:
        csv_dict_reader = DictReader(read_obj, delimiter=";")
        return list(csv_dict_reader)