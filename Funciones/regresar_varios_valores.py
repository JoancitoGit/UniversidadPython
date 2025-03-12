print('*** Regresar una tupla de valores desde una función ***')

# Definición de la función
def persona_mayusculas(nombre, apellido, edad):
    print(f'Esta función regresa varios valores (Tupla): ')
    return (nombre.upper(), apellido.upper(), edad)

# Capturar valores con unpacking
nombre, apellido, edad = persona_mayusculas('Joan', 'García', 33)
print(f'Nombre: {nombre}, Edad: {edad}, Apellido: {apellido}')