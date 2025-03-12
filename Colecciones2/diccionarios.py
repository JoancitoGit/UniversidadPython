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