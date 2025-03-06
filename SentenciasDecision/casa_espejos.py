print('*** Bienvenidos a la casa de los Espejos ***')

edad = int(input('Cuál es tu edad? '))
tienes_miedo_obscuridad = input('Tienes miedo a la oscuridad (Si/No)? ')
tienes_miedo_obscuridad = tienes_miedo_obscuridad.strip().lower() == 'si'

if not tienes_miedo_obscuridad and edad >= 10:
    print('Puedes entrar a la casa de los espejos')
else:
    print('No puedes entrar a la casa de los espejos')