num1 = int(input('Ingresa el primer número: '))
num2 = int(input('Ingresa el segundo número: '))

mayor = num1 if num1 > num2 else num2
print(f'El número mayor entre {num1} y {num2} es: {mayor}')