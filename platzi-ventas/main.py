clients = 'Moisés,Luis,Satoru,Sinval,'

def create_clients(name_client):
    global clients

    if name_client not in clients:
        clients += name_client
        _add_comma()
    else:
        print('Client already is in the client\'s list')


def list_clients():
    global clients
    print(clients)


def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name, update_client_name)
    else:
        print('Client is not clients list')


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name+',','')
    else:
        print('Client is not client list')


def _add_comma():
    global clients
    clients += ','


def _print_welcome():
    print('*' * 30)
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 30)
    print('What would you like to do today?')
    print('[C] Create client')
    print('[D] Delete client')
    print('[U] Update client')


def _get_client_name():
    return input('What is the client name? ')


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
    else:
        print('Invalid command')