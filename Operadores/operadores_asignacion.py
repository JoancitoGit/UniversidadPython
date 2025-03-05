print('***Operadores de Asignación ***')
numero = 5
print(f'Valor de numero: {numero}')
numero = 10
print(f'Valor de numero: {numero}')
cadena = 'Saludos desde Python'
print(f'Valor de la cadena: {cadena}')

# Asignacion multiple
x, y, z = 5, 'Hola', -9.15
print(x,y,z)

# Asignacion encadenada
var1 = var2 = var3 = 10
print(var1, var2, var3)

# Intercambio de valores de una variable, sin utilizar variables temporales
x, y = 5, 10
# Aplicando el concepto de asignación multiple, intercambiamos valores
x, y = y, x
print(f' x = {x} y = {y}')

# Recibir multiples valores de la entrada del usuario
nombre, apellido = input('Ingresa tu nombre y apellido separados por coma: ').split(',')
print(f'Nombre = {nombre.strip()}, Apellido = {apellido.strip()}')