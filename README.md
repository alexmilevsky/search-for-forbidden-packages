# search-for-forbidden-packages
Поиск запрещенных пакетов Composer и NPM из CSV списка. <br />
Проходит по composer.lock и package-lock.json и сравнивает с указанными списками из папки data.<br />
Если неизвестна версия пакета, поставьте прочерк '-' в списке. Тогда будет сравнивать вне зависимости от версии

### Запуск
main.py --path=/var/www/example/src/
