from sistema_biblioteca.biblioteca import Biblioteca
from sistema_biblioteca.libro import Libro

print(f'*** Sistema de Bibliotecas ***')

biblioteca_nacional = Biblioteca('Biblioteca Nacional')
print(f'*** Bienvenidos a la {biblioteca_nacional.get_nombre}')

# Definicion de libros
libro1 = Libro('Cien años de soledad', 'Gabriel García Márquez', 'Ficción')
libro2 = Libro('Don QUijote de la Mancha', 'Miguel de Cervantes', 'Comedia')
libro3 = Libro('El amor en los tiempos de Cólera', 'Gabriel García Márquez', 'Ficción')
libro4 = Libro('Pantaleón y las visitadores', 'Mario Vargas Llosa', 'Comedia')
libro5 = Libro('Pedro Páramo','Juan Rulfo', 'Ficción')

# Agregar los libros a la biblioteca
biblioteca_nacional.agregar_libro(libro1)
biblioteca_nacional.agregar_libro(libro2)
biblioteca_nacional.agregar_libro(libro3)
biblioteca_nacional.agregar_libro(libro4)
biblioteca_nacional.agregar_libro(libro5)

# Buscar libros por autor
autor = 'Gabriel García Márquez'
biblioteca_nacional.buscar_libros_por_autor(autor)
biblioteca_nacional.mostrar_todos_los_libros()
biblioteca_nacional.buscar_libros_por_genero('Ficción')