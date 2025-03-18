class Biblioteca:

    def __init__(self, nombre):
        self._nombre = nombre
        self._libros = []

    def agregar_libro(self, libro):
        self._libros.append(libro)

    def buscar_libros_por_autor(self, autor):
        for libro in self._libros:
            if libro.get_autor.lower() == autor.lower():
                self.mostrar_libro(libro)

    def buscar_libros_por_genero(self, genero):
        for libro in self._libros:
            if libro.get_genero.lower() == genero.lower():
                self.mostrar_libro(libro)

    def mostrar_todos_los_libros(self):
        print(f'\nTordos los libros de la bibilioteca: {self._nombre}')
        for libro in self._libros:
            self.mostrar_libro(libro)

    def mostrar_libro(self, libro):
        print(f'Libro -> Título: {libro.get_titulo}, Author: {libro.get_autor}, Género = {libro.get_genero}')

    @property
    def get_nombre(self):
        return self._nombre

    @property
    def get_libros(self):
        return self._libros