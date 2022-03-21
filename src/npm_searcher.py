import json

from src import file_helper
from src.helpers import CommonHelper


class NpmSearcher:
    # Путь до файла с запрещенными пакетами
    CONST_NPM_PACKAGES_CSV = 'data/npm-packages.csv'
    # Словарь с запрещенными пакетами
    forbidden_packages = {}

    def __init__(self, path):
        self.path = path
        self.forbidden_packages = file_helper.get_list_dictionaries_from_csv(NpmSearcher.CONST_NPM_PACKAGES_CSV)

    # Проверка наличия запрещенного пакета в словаре
    def is_package_exist_in_forbidden(self, package):
        for forbidden_package in self.forbidden_packages:
            if package['name'] == forbidden_package['code']:
                # Если не указана версия пакета - возвращаем найденный пакет
                if CommonHelper.is_package_under_warning(package['version'], forbidden_package['version']):
                    return forbidden_package

        return None

    # Поиск запрещенных пакетов в конкретном файле
    def get_forbidden_packages_by_file(self, file):
        finded_packages = []

        with open(file) as f:
            decoded_package_list = json.load(f)
            for package in decoded_package_list['dependencies']:
                packageDict = decoded_package_list['dependencies'][package]
                # Делаем цельный словарь
                packageDict['name'] = package

                forbidden_package = self.is_package_exist_in_forbidden(packageDict)
                if forbidden_package is not None:
                    result = {
                        "forbidden_package": forbidden_package,
                        "package_installed": packageDict
                    }
                    finded_packages.append(result)

        return finded_packages

    # Возвращает найденные пакеты с группировкой по файлам
    def get_all_forbidden_packages_with_group(self):
        grouped_packages = []

        # Достаем lock файлы
        lock_files = file_helper.find_files(self.path, "package-lock.json")
        for lock_file in lock_files:
            # Находим вредительские компоненты внутри файла
            finded_packages = self.get_forbidden_packages_by_file(lock_file)
            if finded_packages:
                grouped_packages.append({
                    'file': lock_file,
                    'packages': finded_packages
                })

        return grouped_packages
