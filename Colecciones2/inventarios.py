print('*** Sistema de Inventarios ***')

inventario = []
numero_productos = int(input('Cuantos productos quieres agregar? '))

for indice in range(numero_productos):
    print(f'Proporciona los valores del producto {indice + 1}: ')
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))

    # Creamos el diccionario con el detalle del producto
    producto = {'id': indice + 1, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
    inventario.append(producto)

# Mostrar el inventario inicial
print(f'Inventario inicial:\n {inventario}')
