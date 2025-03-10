print('*** Aplicación Contraseña Válida ***')

salir = False
password = ''

while not salir:
    password = input('Ingresa tu contraseña, debe de contener al menos 6 caracteres: ')
    if len(password) <= 5:
        print('Debes ingresar un contraseña de al menos 6 caracteres!!')
    else:
        print(f'Tu contraseña es: {password} y es correcta!')
        salir = True

