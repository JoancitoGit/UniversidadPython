print('*** Sistema Descuentos VIP ***')

NO_PRODUCTOS_DESCUENTO = 10
cantidad_productos = int(input('Cuantos productos compraste hoy? '))
tiene_mempresia = input('Tienes la membresía de la tienda (Si/No)? ')

es_elegible_descuento = (cantidad_productos >= NO_PRODUCTOS_DESCUENTO
                         and tiene_mempresia.strip().lower() == 'si')

print(f'Tienes acceso al destuento VIP? {es_elegible_descuento}')
