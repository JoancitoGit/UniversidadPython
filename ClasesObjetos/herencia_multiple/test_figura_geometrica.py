from herencia_multiple.cuadrado import Cuadrado
from herencia_multiple.rectangulo import Rectangulo

print('Creación Objeto Cuadradado'.center(50, '-'))
cuadrado1 = Cuadrado(lado = 15, color = 'rojo')
print(f'Cálculo área cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creación Objeto Rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(ancho = 13,alto = 8, color = 'verde')
print(f'Cálculo área rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)