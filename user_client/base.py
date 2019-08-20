import json

def address_parser(file):
    with open(file) as json_file:
        parsed = json.loads(json_file.read())
        return parsed['server']['address']