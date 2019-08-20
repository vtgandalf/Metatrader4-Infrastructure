import json

def address_parser(file):
    with open(file) as json_file:
        parsed = json.loads(json_file.read())
        return parsed['server']['address']
        # for client in parsed['clients']:
        #     address = client['address']
        #     list_all_clients.append(address)
        #     list_available_clients.append(address)