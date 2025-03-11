print('*** Combinación de Listas Y Tuplas ***')

# Definir una lista que almacena tuplas de productos
productos = [
    ('P001', 'Camiseta', 20.00),
    ('P002', 'Jeans', 30.00),
    ('P003', 'Sudadera', 40.00)
]

# Imprimir la información de cada producto
# Y Además calculamos el preci ototal

precio_total = 0

print('Informacion de los productos: ')
for producto in productos:
    id, descripcion, precio = producto # Unpacking
    print(f'Producto: id = {id}, descripcion = {descripcion}, precio = ${precio}')
    precio_total += precio # producto[2]
print(f'Precio total de los productos: ${precio_total}')
