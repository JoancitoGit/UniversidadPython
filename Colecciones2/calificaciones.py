print('*** Sistema Calificaciones ***')

calificaciones = []
promedio = 0

numero_calificaciones = int(input('Ingresa el número de calificaciones: (1 - n): '))
for calificacion in range(numero_calificaciones):
    actual = float(input(f'Ingresa la calificación #{calificacion + 1}: '))
    calificaciones.append(actual)
    promedio += calificaciones[calificacion]

print(f'El promedio de tus calificaciones: {calificaciones} es = {promedio/numero_calificaciones}')