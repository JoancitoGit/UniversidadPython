from herencia_multiple.cuadrado import Cuadrado
from herencia_multiple.figura_geometrica import FiguraGeometrica
from herencia_multiple.rectangulo import Rectangulo

# no se puede instanciar una clase abstracta
# figura = FiguraGeometrica()

print('Creación Objeto Cuadradado'.center(50, '-'))
cuadrado1 = Cuadrado(lado = -10, color = 'rojo')
print(f'Cálculo área cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creación Objeto Rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(ancho = 9,alto = 8, color = 'verde')
rectangulo1.ancho = 15
print(f'Cálculo área rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

print(Cuadrado.mro())