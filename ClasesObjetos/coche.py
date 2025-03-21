# Definimos la clase coche
class Coche:

    def __init__(self, marca, modelo, color):
        self._marca = marca
        self._modelo = modelo
        self._color = color

    def conducir(self):
        print(f'''Conduciendo el coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}
        ''')

    #def get_marca(self):
    #    return self._marca
    @property # Definir el metodo get de manera mas pythonica
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

# Programa principal

if __name__ == '__main__':
    # Creacion de un primer coche
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()
    coche1.modelo = 'Suburban'
    coche1.marca = 'Chrisler'
    coche1.color = 'Rojo'
    coche1.conducir()
    # Atributo de marca del coche 1
    coche1.marca = 'Yaris 3'
    print(f'Atributos del coche 1: {coche1.__dict__}')
    print(f'Atributo marca coche1: {coche1.marca}')
    # Intentar agregar un nuevo atributo
    setattr(coche1, 'nuevo_atributo', 'Valor nuevo atributo')
    print(coche1.nuevo_atributo)
    # Segundo objeto
    coche2 = Coche('Chevrolet', 'Trax', 'Blanco')
    coche2.conducir()
    #print(f'Nuevo atributo coche2 {coche2.nuevo_atributo}')

