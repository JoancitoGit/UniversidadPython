print('*** Obtener Coordenadas x,y,z ***')

def obtener_coordenadas():
    x,y,z = 10, 20, 30
    return (x, y, z)

# Llamar la función
resultado = obtener_coordenadas()
print(resultado)

# Unpacking de la tupla
x,y,z = obtener_coordenadas()
print(f'Las coordenadas son: x: {x}, y: {y}, z: {z}')