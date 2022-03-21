from src.composer_searcher import ComposerSearcher
from src.npm_searcher import NpmSearcher


class PackageSearcher:
    def __init__(self, search_path):
        self.search_path = search_path

    # Форматирование вывода сгруппированных пакетов
    def printFormattedGroup(self, grouped_packages):
        print('-------')
        for file_group in grouped_packages:
            print('Найдены запрещенные пакеты в файле: ' + file_group['file'])
            for package in file_group['packages']:
                forbidden_description = 'Пакет ' + package['forbidden_package']['code']
                if package['forbidden_package']['version'] != '-':
                    forbidden_description += ' с версии ' + package['forbidden_package']['version']
                forbidden_description += ' небезопасен. Описание проблемы: ' + package['forbidden_package'][
                    'description']
                print('Установлен: {0} {1}. {2}'.format(package['package_installed']['name'],
                                                        package['package_installed']['version'],
                                                        forbidden_description))

    def execute(self):
        npm_searcher = NpmSearcher(self.search_path)
        grouped_npm_packages = npm_searcher.get_all_forbidden_packages_with_group()
        if grouped_npm_packages:
            self.printFormattedGroup(grouped_npm_packages)

        composer_searcher = ComposerSearcher(self.search_path)
        grouped_composer_packages = composer_searcher.get_all_forbidden_packages_with_group()
        if grouped_composer_packages:
            self.printFormattedGroup(grouped_composer_packages)

        if not grouped_npm_packages and not grouped_composer_packages:
            print("Вредоносных пакетов не найдено.")
