import sys

clients = [
    {
        'name': 'Moisés',
        'company': 'Cerba-LCA',
        'email': 'mescurra@cerba-lca.com.br',
        'position': 'Analista de Sistemas'
    },
    {
        'name': 'Henrique',
        'company': 'Cerba-LCA',
        'email': 'hvieira@cerba-lca.com.br',
        'position': 'Coordenador de TI Brasil'
    },{
        'name': 'Fabiano',
        'company': 'Cerba-LCA',
        'email': 'fstellita@cerba-lca.com.br',
        'position': 'Coordenador de implantação'
    },{
        'name': 'Davi',
        'company': 'Cerba-LCA',
        'email': 'dRodigues@cerba-lca.com.br',
        'position': 'Suporte Técnico'
    }
]

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
        list_clients()
    elif command == 'D':
        client_name = int(_get_client_field('Id'))
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_field('name')
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