print('*** SISTEMA DE ESTACIÓN DEL AÑO ***')

mes = int(input('Ingresa el número del mes (entre 1 y 12) en el que te encuentras: (ej. 1 = Enero) '))
if mes == 1 or mes == 2 or mes == 12:
    print('La estación en la que te encuentras es Invierno')
elif mes == 3 or mes == 4 or mes == 5:
    print('La estación en la que te encuentas es Primavera')
elif mes == 6 or mes == 7 or mes == 8:
    print('La estación en la que te encuentras es Verano')
elif mes == 9 or mes == 10 or mes == 11:
    print('La estación en la que te encuentras es Otoño')
else:
    print('Estación desconocida')
