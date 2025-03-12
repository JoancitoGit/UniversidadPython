print('*** Agenda de Contactos ***')

agenda = {
    'Carlos': {
        'telefono': '3112038196',
        'email': 'carlos@mail.com',
        'direccion': 'Calle Principal'},
    'María': {
        'telefono': '322222222',
        'email': 'maria@mail.com',
        'direccion': 'Calle Secundaria'},
    'Pedro': {
        'telefono': '3111238931',
        'email': 'pedro@mail.com',
        'direccion': 'Calle Final'}
}

print(agenda)

# Acceder a la información de un contacto en espcifico
print(f'''Información del contacto de María:
Teléfono: {agenda["María"]["telefono"]},
Email: {agenda["María"]["email"]},
Dirección: {agenda["María"]["direccion"]}
''')

# Agregar un nuevo contacto
agenda['Ana'] = {
    'telefono': '3222309681',
    'email': 'ana@mail.com',
    'direccion': 'Viene del Futuro'
}

print(agenda)

# Eliminar un contacto existente
agenda.pop('Pedro')
del agenda['Ana']
print(agenda)

# Mostramos los contactos de la agenda
print('\nContactos en la Agenda')
for nombre, detalles in agenda.items():
    print(f'''Nombre: {nombre}
              Telefono: {detalles.get('telefono')}
              Email: {detalles.get('email')}
              Dirección: {detalles.get('direccion')}''')