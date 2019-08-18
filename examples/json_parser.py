import json

list_all_clients = list()
list_available_clients = list()

def address_parser(file):
    with open(file) as json_file:
        parsed = json.loads(json_file.read())
        # print(parsed['clients'])
        for client in parsed['clients']:
            address = client['address']
            list_all_clients.append(address)
            list_available_clients.append(address)

address_parser('testing.json')
list_available_clients.remove('client.address')
print(list_all_clients)
print(list_available_clients)