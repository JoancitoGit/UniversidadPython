print('*** Playlist de Canciones ***')

# Creamos la lista vacía
lista_reproduccion = []

numero_canciones = int(input('Cuantas canciones deseas agregar? '))

# Iteramos cada elemento de la lista para agregar un nuevo elemento
for indice in range(numero_canciones):
    cancion = input(f'Proporciona la cancion {indice + 1}: ')
    lista_reproduccion.append(cancion)

# Ordenar la lista en orden alfabetico. sort
lista_reproduccion.sort() # reverse=True


# Mostrar la lista iterando cada uno de los elementos
for cancion in lista_reproduccion:
    print(cancion)