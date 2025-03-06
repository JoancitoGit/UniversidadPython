print('*** Sistema de Reserva de Hotel ***')

nombre_cliente = input('Ingresa tu nombre: ')
dias_estadia = int(input('Cuantos días te piensas hospedar? '))
cuarto_mar = input('Desea que su cuarto tenga vista al mar? (Si/No) ').strip().lower()

# Realizamos las comparaciones
precio_habitacion = 150.50 if cuarto_mar == 'no' else 190.50

print('----------Detalles de la Reservación----------')
print(f'Cliente: {nombre_cliente}')
print(f'Días de estadía: {dias_estadia}')
print(f'Costo total: ${precio_habitacion*dias_estadia}')
print(f'Habitación con vista al mar: {cuarto_mar}')

