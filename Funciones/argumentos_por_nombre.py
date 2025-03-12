print('*** funcion con argumentos por nombre ***')

def imprimir_persona(nombre, apellido='', edad=0):
    print(f'Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')

# Primero llamamos la función pasando los argumentos de manera posicional
imprimir_persona('Joan','García',33)

#Llamar la funcion usando argumentos por nombre
imprimir_persona(nombre='Joan',apellido='García',edad=33)

# Llamar la función usando argumentos por nombre pero intercambiando el orden
imprimir_persona(edad=50, nombre='Nacho', apellido='Ortíz')

# Argumentos con valores por default
imprimir_persona(nombre='Carlos')
imprimir_persona(nombre='Joan', apellido='Cedano')
imprimir_persona(nombre='Joan', apellido='Cedano',edad=58)