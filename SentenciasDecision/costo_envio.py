print('*** Sistema de Envíos***')

NACIONAL = 10
INTERNACIONAL = 20

destino = input('El destino del paquete es nacional o internacional? ').strip().lower()
peso = int(input('Cuantos kilos pesa el paquete? '))

costo = NACIONAL * peso if destino == 'nacional' else INTERNACIONAL * peso

print(f'El precio de tu paquete {destino} con un peso de {peso} kg es de ${costo}')
