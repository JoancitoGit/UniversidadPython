print('*** Imprimir del 1 al 5 de forma recursiva')

# Definimos la funcion recursiva
def funcion_recursiva(numero):
    # Caso base
    if numero == 1:
        print(numero, end=' ')
    else: # Caso recursivo
        funcion_recursiva(numero - 1)
        print(numero, end = ' ')

funcion_recursiva(5)
