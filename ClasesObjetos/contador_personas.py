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

if __name__ == '__main__':
    print('*** Ejemplo Contador de Objetos de tipo Persona ***')
    persona1 = Persona('Joan', 'García')
    persona2 = Persona('Diana', 'García')

    persona1.mostrar_persona()
    persona2.mostrar_persona()