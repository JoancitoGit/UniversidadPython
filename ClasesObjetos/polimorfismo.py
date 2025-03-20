class Animal:

    def hacer_sonido(self):
        print('Hago un Pitido')

class Perro(Animal):

    def hacer_sonido(self):
        print('Puedo Ladrar')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo Maullar')

print('*** Ejemplo Polimorfismo ***')
print('Clase Padre Animal: ')
animal1 = Animal()
animal1.hacer_sonido()

print('Clase Hija Perro: ')
perro1 = Perro()
perro1.hacer_sonido()

print('Clase Hija Gato: ')
gato1 = Gato()
gato1.hacer_sonido()