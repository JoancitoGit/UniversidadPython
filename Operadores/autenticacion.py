# Programa de login
print('*** LOGIN ***')
USUARIO_CORRECTO = 'Joan'
CONTRASENIA_CORRECTA = 'J04M05A19G91C'

usuario = input('Ingresa tu usuario: ')
contrasenia = input('Ingresa tu contraseña: ')

acceso = usuario.strip().lower() == USUARIO_CORRECTO.strip().lower() and contrasenia.strip().upper() == CONTRASENIA_CORRECTA
print(f'Acceso: {acceso}')