print('--- Calculadora de Impuestos ---')

# Funcion que calcula el total de un pago incluyendo el impuesto
def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + (pago_sin_impuesto*(impuesto/100))
    return pago_total

# Ejecutamos la función
pago_sin_impuesto = float(input('Ingresa la cantidad para calcular su impuesto: '))
impuesto = float(input('Proporcione el monto del impuesto: '))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'Pago con impuesto: {pago_con_impuesto}')
