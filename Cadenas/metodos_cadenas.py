# Metodos cadenas

cadena1 = 'Hola Mundo'
print(f'Cadena original: {cadena1}')
mayusculas = cadena1.upper()
minusculas = cadena1.lower()


print(f'Cadena en mayusculas {mayusculas}')
print(f'Cadena en minusculas {minusculas}')

cadena2 = '    Juan Perez    '
print(f'Cadena con espacios: {cadena2}')
print(f'Cadena sin espacios: {cadena2.strip()}') # el método .strip() elimina espacios en blanco al inicio y al final
