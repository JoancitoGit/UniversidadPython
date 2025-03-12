print('*** Función par ***')

# Funcion para saber si un numeros es par o no
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Llamamos a la funcion
if __name__ == '__main__':
    numero = int(input('Proporciona un valor númerico: '))
    print(f'Numero par? {es_par(numero)}')