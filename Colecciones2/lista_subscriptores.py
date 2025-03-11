print('*** Lista de Suscriptores ***')

# Definimos el set inicial
# suscriptores = {} # Aqui se define un diccionario vacío
suscriptores = set() # Definimos un set vacio

numero_suscriptores = int(input('Ingresa la cantidad de suscriptores iniciales: '))

for _ in range(numero_suscriptores):
    suscriptores.add(input('Nuevo suscriptor (email): '))


print(f'Lista de suscriptores inicial: {suscriptores}')

# Verifica si un nuevo suscriptor ya está en la lista
nuevo_suscriptor = input('Proporciona el nuevo suscriptor: ')
if nuevo_suscriptor in suscriptores:
    print(f'El nuevo suscriptor ya está en la lista: {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptor se ha agregado a la lista: {nuevo_suscriptor}')

print(f'Lista de suscriptores final: {suscriptores}')

# Eliminamos nu suscriptor
suscriptor_eliminar = input('Porporciona el suscriptor a eliminar: ')
suscriptores.remove(suscriptor_eliminar)
print(f'El suscriptor: {suscriptor_eliminar} ha sido eliminado de la lista')
print(f'Lista de suscriptores: {suscriptores}')

# Verificamos la cantidad total de suscriptores
print(f'Cantidad total de suscriptores: {len(suscriptores)}')

# mostramos todos los suscriptores
for suscriptor in suscriptores:
    print(f' - {suscriptor}')
