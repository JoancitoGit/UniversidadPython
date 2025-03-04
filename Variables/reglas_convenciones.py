# Reglas y convenciones en nombres de variables

# Ejemplos de reglas estrictas
nombre_usuario = 'Juan Perez'
# SyntaxError: 1nombre_usuario = "Karla Gomez"

# No podemos usar palabras reservadas
# SyntaxError: class = 'Mi clase'
klass = 'Mi Clase'

# Sensibles a mayusculas y minusculas
nombre = 'Joan'
Nombre = 'Manuel'
print(nombre, Nombre)

# snake case
nombre_completo = "Joan Manuel Alexander García Cedano"
print(nombre_completo)

# prefijos y sufijos
es_casado = True
nombre_txt = 'archivo.txt'