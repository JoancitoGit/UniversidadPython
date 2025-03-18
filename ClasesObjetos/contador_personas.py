class Persona:

    # Atributo clase
    contador_personas = 0

    def __init__(self, nombre, apellido):
        # Incrementamos el valor del atributo de clase
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'Persona: {self.id}, {self.nombre}, {self.apellido}')

    @staticmethod
    def get_contador_personas_estatico():
        print('Método Estatico')
        return Persona.contador_personas

    @classmethod
    def get_contador_personas_clase(cls):
        print('Método Estatico Pythonico')
        return cls.contador_personas

if __name__ == '__main__':
    print('*** Ejemplo Contador de Objetos de tipo Persona ***')
    persona1 = Persona('Joan', 'García')
    persona2 = Persona('Diana', 'García')

    persona1.mostrar_persona()
    persona2.mostrar_persona()

    # Imprimir el valor del contador de objetos de personas
    print(f'Contador objetos Persona (static): {Persona.get_contador_personas_estatico()}')
    print(f'Contador objetos Persona (pythonico): {Persona.get_contador_personas_clase()}')