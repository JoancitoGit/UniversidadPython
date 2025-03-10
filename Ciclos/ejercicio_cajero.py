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
        retiro = float(input('Cuanto deseas retirar?: '))
        if retiro <= saldo:
            saldo -= retiro
            print(f'Tu nuevo saldo es: ${saldo:.2f\n}')
        else:
            print(f'No cuentas con el saldo suficiente, Saldo actual es: ${saldo:.2f}\n')
        saldo -= retiro
    elif(opcion == 3):
        deposito = float(input('Cuanto deseas depositar?: '))
        saldo += deposito
    elif(opcion == 4):
        print('Hasta luego!')
        salir = True
    else:
        print('Selecciona una opción válida')