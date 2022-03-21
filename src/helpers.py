from packaging import version


class CommonHelper:
    @staticmethod
    # Если версия пакета больше или равна, то пакет попадает
    def is_package_under_warning(installed_package, forbidden_package):
        if forbidden_package == '-':
            # Если прочерк, считаем все версии заведомо проблемные
            return True
        return version.parse(installed_package) >= version.parse(forbidden_package)
