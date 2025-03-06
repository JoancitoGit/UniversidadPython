print(f'*** Sistema de Descuentos ***')

compra = int(input('Cual fue el monto de tu compra? '))
miembro = input('Eres miembro de la tienda (si/no) ').strip().lower()

if compra >= 1000 and miembro == 'si':
    print(f'Felicidades, has obtenido un descuento del  10%')
    print(f'Monto de la compra: ${compra}')
    descuento = compra * .10
    print(f'Monto del descuento: ${descuento}')
    print(f'Monto final de la compra con descuento: ${compra-descuento}')
elif compra < 1000 and miembro == 'si':
    print(f'Felicidades, has obtenido un descuento del  5%')
    print(f'Monto de la compra: ${compra}')
    descuento = compra * .05
    print(f'Monto del descuento: ${descuento}')
    print(f'Monto final de la compra con descuento: ${compra - descuento}')
else:
    print(f'No recibes descuento, tu compra fue de: ${compra}')
