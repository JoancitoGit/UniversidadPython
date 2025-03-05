print('*** VALOR DENTRO DE RANGO ***')
valor = int(input('Ingresa un valor entre 0 y 5: '))
MINIMO = 0
MAXIMO = 5
esta_en_rango = valor >= 0 and valor <= 5
esta_en_rango = MINIMO <= valor <= MAXIMO
print(f'El valor está dentro del rango?: {esta_en_rango}')