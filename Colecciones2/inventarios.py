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

# Buscar un producto por el id
id_buscar = int(input('\nIngresa el ID del producto a buscar: '))
producto_encontrado = None
for producto in inventario:
    if producto.get('id') == id_buscar:
        producto_encontrado = producto
        break

if producto_encontrado is not None:
    print('Información de producto encontrado: ')
    print(f'''Id: {producto_encontrado.get('id')},
    Nombre: {producto_encontrado.get('nombre')},
    Precio: {producto_encontrado.get('precio')},
    Cantidad: {producto_encontrado.get('cantidad')}''')
else:
    print(f'Producto con id {id_buscar} No encontrado')

# Mostrar inventario detallado
print(f'\n--- Inventario Detallado ---')
for producto in inventario:
    print(f'''Id: {producto.get('id')}
    Nombre: {producto.get('nombre')}
    Precio: ${producto.get('precio'):.2f}
    Cantidad: {producto.get('cantidad')}''')