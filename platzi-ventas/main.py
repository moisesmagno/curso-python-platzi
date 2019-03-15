import sys

clients = ['Moisés','Candy','Salvador','Carmen','seila']

def create_clients(name_client):
    global clients

    if name_client not in clients:
        clients.append(name_client)
    else:
        print('Client already is in the client\'s list')


def list_clients():
    global clients

    for idx, client in enumerate(clients):
        print('{}: {}'.format(idx, client))


def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = update_client_name
    else:
        print('Client is not clients list')


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        print('Client is not client list')


def search_client(client_name):
    global clients

    for client in clients:
        if client != client_name:
            continue
        else:
            return True


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
    _print_welcome()

    command = input('select the command [C] or [D] or [U]: ').upper()
    if command == 'C':
        client_name = _get_client_name()
        create_clients(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input('What is the updated client name? ')
        update_client(client_name, update_client_name)
        list_clients()
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