print('--- Convertidor de Temperaturas ---')

def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

# Funcion que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

celsius = float(input('Ingresa la temperatura en Celsius: '))
resultado = celsius_fahrenheit(celsius)

print(f'{celsius} C a F: {resultado:.2f}')

fahrenheit = float(input('Ingresa la temperatura en Fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)

print(f'{fahrenheit} F a C: {resultado}')