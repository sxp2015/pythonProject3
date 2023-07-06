from os.path import relpath, dirname, join
import json


def get_config(name):
    path = join(dirname(relpath(__file__)), 'configs', f'{name}.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
