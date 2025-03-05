# Generador de ID unico
from random import randint

nombre = input('Ingresa el nombre: ')[0:2].upper()
apellido = input('Ingresa tu apellido: ')[0:2].upper()
nacimiento = input('Ingresa año de nacimiento Y-Y-Y-Y: ')[2:4]
random = str(randint(1000, 9999))

print(f'Resultado ID Único: {nombre+apellido+nacimiento+random}')

