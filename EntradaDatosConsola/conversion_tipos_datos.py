# Conversión de tipos de datos

# Convertir cadena a número

numero_cadena = '10'
numero_entero = int(numero_cadena)
print(f'Valor númerico en cadena: {numero_cadena}')
print(f'Cadena a entero: {numero_entero}')

# Convertir de cadena a flotante
numero_cadena = '3.14'
numero_flotante = float(numero_cadena)
print(f'Valor numerico en cadena: {numero_cadena}')
print(f'Cadena a flotante: {numero_flotante}')

# Convertir de numero a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f'Valor cadena a numérico: {numero_entero}')
print(f'Numerico a cadena: {numero_cadena}')

# Convertir a booleano
# Tipo bool es Falso en los siguientes casos
# Si el valor es 0, cadena vacía, o None, entonces regresa False
# Regresa True, si el valor es distinto de 0, si es distinto de cadena vacía
# y también si es distinto de None

numero_entero = 0
booleano = bool(numero_entero)
print(f'Valor de entero a Booleano: {booleano}')

numero_entero = 5
booleano = bool(numero_entero)
print(f'Valor de entero a Booleano: {booleano}')

cadena = ''
booleano = bool(cadena)
print(f'Valor de cadena a Booleano: {booleano}') # Falso, incliye colecciones vacías

cadena = 'Cadena con valor'
booleano = bool(cadena)
print(f'Valor de cadena a Booleano: {booleano}') # True

variable = None
booleano = bool(variable)
print(f'Valor de None a Booleano: {booleano}')