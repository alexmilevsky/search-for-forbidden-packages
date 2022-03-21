import argparse
from src.searcher import PackageSearcher

parser = argparse.ArgumentParser()
parser.add_argument('--path', help='Example: /var/www/example/src/')
args = parser.parse_args()

if args.path is not None:
    package_searcher = PackageSearcher(args.path)
    package_searcher.execute()
else:
    print('Не указан параметр --path=/var/www/example/src/')
