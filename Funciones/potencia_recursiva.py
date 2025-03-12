print('*** Función potencia recursiva ***')

def potencia_recursiva(base, potencia):
    if potencia == 0:
        return 1
    else:
        return base * potencia_recursiva(base, potencia-1)

base = 2
potencia = 2
resultado = potencia_recursiva(base, potencia)
print(resultado)