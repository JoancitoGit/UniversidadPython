# Inmutabilidad en cadenas
cadena1 = 'Hola Mundo'
# [0] = 'S' # No podemos modificar los caracteres
cadena2 = cadena1
cadena1 = 'Adios'
print(cadena1)
print(cadena2)