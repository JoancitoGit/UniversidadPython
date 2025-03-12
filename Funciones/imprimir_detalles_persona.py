print('*** Imprimir detalles de una persona usando kwargs ***')

# Funcion que acepta argumentos variables en forma de llave->valor
def imprimir_detalle_persona(**kwargs):
    print('\nValores recibidos: ')
    for llave, valor in kwargs.items():
        print(f'Llave - {llave}, Valor - {valor}')

# Llamamos la función
imprimir_detalle_persona(nombre='Joan', edad=30, ciudad='CDMX')

