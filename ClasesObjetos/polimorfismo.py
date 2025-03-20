class Animal:

    def hacer_sonido(self):
        print('Hago un Pitido')

class Perro(Animal):

    def hacer_sonido(self):
        print('Puedo Ladrar')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo Maullar')

# Funcion polimorfica
def hacer_sonido_animal(animal): # Duck Typing
    animal.hacer_sonido()


print('*** Ejemplo Polimorfismo ***')
print('Clase Padre Animal: ')
animal1 = Animal()
hacer_sonido_animal(animal1)
print('Clase Hija Perro: ')
perro1 = Perro()
hacer_sonido_animal(perro1)
print('Clase Hija Gato: ')
gato1 = Gato()
hacer_sonido_animal(gato1)
