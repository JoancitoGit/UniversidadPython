print('*** Función Factorial Recursiva ***')

def factorial_recursiva(numero):
    # Caso base, factorial 0! = 1, 1! = 1
    if numero == 0 or numero == 1:
        print(f'El resultado factorial parcial {numero} es: 1')
        return 1
    else: # Caso recursivo
        factorial_parcial = numero * factorial_recursiva(numero - 1)
        print(f'El resultado factorial parcial {numero} es: {factorial_parcial}')
        return factorial_parcial

numero = 100
resultado = factorial_recursiva(numero)
print(f'El factorial de {numero} es: {resultado}')