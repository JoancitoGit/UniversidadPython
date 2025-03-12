print('*** Diccionarios en Python ***')

# Creamos un dict de persona con clave y valor
persona = {
    'nombre': 'Joan',
    'edad': 33,
    'ciudad': 'Tepic',
    'profesion': 'Ingeniero'
}

print(f'Diccionario de persona: {persona}')

# Acceder a los elementos del diccionario
print(f'Nombre: {persona["nombre"]}')
print(f'Edad: {persona.get("edad")}')

# Modificar un valor del diccionario
persona['edad'] = 35
print(f'Diccionario de persona: {persona}')

# Agregar un nuevo elemento
persona['hobby'] = 'Girls'
print(f'Diccionario de persona: {persona}')

# Eliminar un elemento del diccionario
del persona['hobby']
print(f'Diccionario de persona: {persona}')

persona.pop('profesion')
print(f'Diccionario de persona: {persona}')

# Iterar los elementos de un diccionario (llave, valor)
for llave, valor in persona.items():
    print(f'Llave: {llave}, valor: {valor}')

# Obtener los valores
for valor in persona.values():
    print(f'Valores: {valor}')

# Obtener llaves
for keys in persona.keys():
    print(f'Keys: {keys}')