print('*** SISTEMA DE CALIFICACIONES ***')

calificacion = int(input('Ingresa tu calificación: '))
calificacion_letra = None
if calificacion >= 9 and calificacion <= 10:
    calificacion_letra = 'A'
elif calificacion >= 8 and calificacion < 9:
    calificacion_letra = 'B'
elif calificacion >= 7 and calificacion < 8:
    calificacion_letra = 'C'
elif calificacion >= 6 and calificacion < 7:
    calificacion_letra = 'D'
elif calificacion >= 0 and calificacion < 6:
    calificacion_letra = 'F'
else:
    print('Valor Desconocido')

print(f'Tu calificación en número es: {calificacion} y en letra es {calificacion_letra}')

