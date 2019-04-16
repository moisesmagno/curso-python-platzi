PASSWORD = '123456'

# *****PRIMEIRO EXEMPLO*****
def password_required(func):
    def wrapper():
        password = input('Digite a senha: ')

        if PASSWORD == password:
            return func()
        else:
            print('La contraseña no es correcta!')

    return wrapper

@password_required
def needs_password():
    print('La contraseña está correcta!!')


# *****SEGUNDO EXEMPLO*****



if __name__ == '__main__':
    #needs_password()