print(f'*** Sistema de ADministración de Cuentas ***')

seleccion = 0
while seleccion != 3:
    print("""Menu:
                1. Crear Cuenta
                2. Eliminar Cuenta
                3. Salir""")
    seleccion = int(input('Escoje una opción: '))
    if(seleccion == 1):
        print('Creando tu cuenta...')
    elif(seleccion == 2):
        print('Eliminando tu cuenta...')
    else:
        seleccion=0
