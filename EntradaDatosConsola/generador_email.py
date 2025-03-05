
nombre = input('Ingresa tu nombre: ')
apellido = input('Ingresa tu apellido: ')
empresa = input('Ingresa el nombre de tu empresa: ')
dominio = input('Ingresa tu dominio: ej. com.mx: ')

nombre_convertido = nombre.replace(' ','.').lower()
apellido_convertido = apellido.replace(' ', '.').lower()
empresa_convertido = empresa.replace(' ', '').lower()

print(f'Resultado: {nombre_convertido+'.'+apellido_convertido}@{empresa_convertido}.{dominio}')

