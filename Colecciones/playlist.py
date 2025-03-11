print('*** Playlist de Canciones ***')

# Creamos la lista vacía
lista_reproduccion = []

# Empezamos a agregar canciones

lista_reproduccion.append('Hotel California - Eagles')
lista_reproduccion.append('Staying Alive - Bee Gees')
lista_reproduccion.append(('Dream on - Aerosmith'))

# Ordenar la lista en orden alfabetico. sort
lista_reproduccion.sort() # reverse=True

# Mostrar la lista de canciones
print(f'\n Lista de Reproducción en orden alfabético: ')
print(lista_reproduccion)

# Mostrar la lista iterando cada uno de los elementos
for cancion in lista_reproduccion:
    print(cancion)