import sys
import csv
import os

CLIENT_TABLE = 'clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []

def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

    os.remove(CLIENT_TABLE)
    os.rename(tmp_table_name, CLIENT_TABLE)


def create_clients(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')


def list_clients():
    global clients

    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
                uid=idx,
                name=client['name'],
                company=client['company'],
                email=client['email'],
                position=client['position']
            )
        )


def update_client(client_name, update_client_name):
    global clients

    for client in clients:
        if client_name == client['name']:
            client['name'] = update_client_name
            break
        else:
            continue

    print('***** Client is not clients list *****')


def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[client_id]
            break


def search_client(client_name):
    global clients

    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}? '.format(field_name))

    return field


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name? ')

        if client_name == 'exit':
            break

    if not client_name:
        sys.exit()

    return client_name


def _print_welcome():
    print('*' * 30)
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 30)
    print('What would you like to do today?')
    print('[L] List client')
    print('[C] Create client')
    print('[D] Delete client')
    print('[U] Update client')
    print('[S] Search client')


if __name__ == '__main__':
    _initialize_clients_from_storage()
    _print_welcome()

    command = input('select the command [L] or [C] or [D] or [U] or [S]: ').upper()
    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position')
        }

        create_clients(client)
    elif command == 'D':
        client_name = int(_get_client_field('Id'))
        delete_client(client_name)
    elif command == 'U':
        client_name = _get_client_field('name')
        update_client_name = input('What is the updated client name? ')
        update_client(client_name, update_client_name)
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The client is in the Client\'s list :)')
        else:
            print('The client: {} is not the Client\'s list!'.format(client_name))
    elif command == 'L':
        list_clients()
    else:
        print('Invalid command')

    _save_clients_to_storage()