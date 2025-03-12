# Definicion de una clase
class Persona:

    # Constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def inicializar_persona(self, nombre, apellido):
        # Creamos los atributos de la clase
        self.nombre = nombre;
        self.apellido = apellido;

    def mostrar_persona(self):
        print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')
        print(f'Dirección de memoria Self: {id(self)}')
        print(f'Dirección de memoria hexadecimal Self: {hex(id(self))}')

# Creacion de objetos
if __name__ == '__main__':
    # Creacion de un primer objeto
    persona1 = Persona('Joan','García') # Crea un objeto vacío en memoria
    persona1.mostrar_persona()

    # Creamos un segundo objeto
    persona2 = Persona('Ian','Sanchez')
    persona2.mostrar_persona()

    persona3 = Persona('Alexander', 'Cedano')
    persona3.mostrar_persona()