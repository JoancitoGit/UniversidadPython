print('*** Ejercicio Suma Acumulativa ***')

MAXIMO = 5
numero = 1
suma = 0

while numero <= MAXIMO:
    print(f'\nAcumulador suma + numero -> {suma} + {numero}')
    suma += numero
    numero += 1

print(f'\nResultado de la suma acumulada: {suma}')