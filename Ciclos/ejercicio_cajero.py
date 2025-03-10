print('*** Aplicacion de Cajero Automatico ***')

saldo = 10000
salir = False

while not salir:
    print('''Operaciones que puedes realizar:
    1. Consultar Saldo
    2. Retirar
    3. Depositar
    4. Salir''')
    opcion = int(input('Selecciona una opción: '))
    if(opcion == 1):
        print(f'Tu saldo es de: ${saldo}')
    elif(opcion == 2):
        retiro = int(input('Cuanto deseas retirar?: '))
        saldo -= retiro
    elif(opcion == 3):
        deposito = int(input('Cuanto deseas depositar?: '))
        saldo += deposito
    elif(opcion == 4):
        print('Hasta luego!')
        salir = True
    else:
        print('Selecciona una opción válida')