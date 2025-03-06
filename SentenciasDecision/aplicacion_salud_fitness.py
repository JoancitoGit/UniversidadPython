print('*** Aplicación de Salud y Fitness ***')

# CONSTANTES
META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04 # Valor aproximado, son kilocalorias

# Pedimos los valores al uduario
nombre_usuario = input('Cuál es tu nombre? ')
pasos_diarios = int(input('Cuántos pasos has caminado hoy? '))

# Verificar si el usuario alcanzó la meta de los pasos diarios
meta_alcanzada = pasos_diarios >= META_PASOS_DIARIOS
meta_alcanzada_txt = 'Sí' if meta_alcanzada else 'No'
# Calculamos las calorías quemadas
calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

# Mostramos la información
print(f'\nUsuario: {nombre_usuario}')
print(f'Pasos dados hoy: {pasos_diarios}')
print(f'Calorías quemadas: {calorias_quemadas} kcal')
print(f'Meta de pasos diarios alcanzada: {meta_alcanzada_txt}')
print(f'La meta de pasos diarios es de : {META_PASOS_DIARIOS}')
