print('*** Suma con argumento variables ***')

# Funcion sumar que acepta argumentos variables
def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

# llamamos a la función sumar
resultado = sumar(1,2,3,4,5)
print(f'Resultado de la suma: {resultado}')
