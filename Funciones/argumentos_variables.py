print('*** Argumentos Variables ***')

def superheroe_superpoderes(superheroe, nombre, *args):
    print(f'Superheroe: {superheroe} - {nombre} - {args}')
    #Iteramos los sueprpoderes
    for superpoder in args:
        print(f'\nSuperpoder: {superpoder}')

superheroe_superpoderes('Superman', 'Peter Parker', 'Vista Laser', 'Aliento Congelador', 'Super Fuerza')

# Es opcional enviar agumentos variables
superheroe_superpoderes('Mi Vecino', 'Juan Pérez')