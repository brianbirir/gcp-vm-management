import json


def prettify_json(result):
    print(json.dumps(result, indent=4, sort_keys=True))
