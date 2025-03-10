print('*** Calculadora en Python ***')

salir = False
num1 = None
num2 = None

while not salir:
    print('''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir''')
    opcion = int(input('Escoje una opción: '))
    if(opcion == 1):
        num1 = float(input('Ingresa el primer valor: '))
        num2 = float(input('Ingresa el segundo valor: '))
        print(f'La suma de {num1} + {num2} = {num1+num2}')
    elif opcion == 2:
        num1 = float(input('Ingresa el primer valor: '))
        num2 = float(input('Ingresa el segundo valor: '))
        print(f'La resta de {num1} - {num2} = {num1 - num2}')
    elif opcion == 3:
        num1 = float(input('Ingresa el primer valor: '))
        num2 = float(input('Ingresa el segundo valor: '))
        print(f'La multiplicación de {num1} * {num2} = {num1 * num2}')
    elif opcion == 4:
        num1 = float(input('Ingresa el primer valor: '))
        num2 = float(input('Ingresa el segundo valor: '))
        print(f'La división de {num1} / {num2} = {num1 / num2}')
    elif opcion == 5:
        print('Saliendo de la calculadora, hasta pronto!')
        salir = True
    else:
        print('Ingresa una opción válida.')