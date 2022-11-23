'''todo SE DEBE RESOLVER CON FUNCIONES: acciones:diseñar una lista tipo spotify que pueda anexar artista y 
cancion pero cada cancion debe de tener genero y duracion
-buscar artista
-buscar cancion
-eliminar artista
-ordenar alfabeticamente
-elque tiene mas canciones
-el que tiene la cancion mas larga
-el que tiene la cancion mas corta'''
#menu=input('Bienvenido a spotify\n Elige alguna de las siguientes opciones\n MENU\n 1=Anexar Artista\n 2=Buscar artista\n 3=Buscar cancion\n 4=Eliminar artista\n')

spotify={}

def artista(spotify):
    ar=input('ingrese el nombre del artista:')
    gen=input('ingrese el genero:')
    can=input('ingrese la cancion del artista:')


    dur=float(input('ingrese la duracion de la cancion en m/s'))
    if ar not in spotify:
        spotify.update({ar:{'genero':gen,
                        'cancion':[can,[dur]]}})
    else:
        print('entro')
        can=input('ingrese la cancion del artista:')
        dur=float(input('ingrese la duracion de la cancion en m/s'))
        spotify[ar].append({'cancion':[can,[dur]]})

    return spotify


def buscarArts(spotify):
    buscar=input('¿Qué artista desea buscar')
    for i in sorted(spotify.keys()):
        if buscar==i:
            print('el artista buscado se encuentra en la lista')
        else:
            print('el artista',buscar,'no se encuentra en la lista de canciones spotify')
    return spotify
   
def buscarcancion(spotify):
    buscar=input('¿Qué cancion desea buscar')
    for i in sorted(spotify.values()):
        if buscar==i:
            print('la cancion buscada se encuentra en la lista')
        else:
            print('la cancion',buscar,'no se encuentra en la lista de canciones spotify')
def eliminar_artista(spotify):
    buscar=input('Escribe el artista que desea borrar')
    if buscar in spotify['artista']:
        spotify.pop(buscar)
    else:
        print('El artista no se encuentra en spotify')
    return spotify
def cancion_m(spotify):
    for i in spotify['cancion']:
        larga=max(spotify[i])
    print(f'La cancion mas larga es {larga}')
def cancion_chiquita(spotify):
    for i in spotify['cancion']:
        chiquita=max(spotify[i])
    print(f'La cancion mas corta es {chiquita}')
def ordenar(spotify):
    ordenar1=sorted(spotify['artista'])
    print('los artistas ordenados son',ordenar1)
#print(todas(spotify))
menu=int(input('Bienvenido a spotify \n Elige alguna de las siguientes opciones \n MENU \n 1-Agregar playlist \n 2-Buscar artista \n 3-Buscar cancion \n 4-Eliminar artista \n 5-Cancion mas larga \n 6-Cancion mas corta \n 7-Ordenar alfabeticamente \n 8-Salir \n'))
while menu!=8:
    match menu:  
        case 1:
            artista(spotify)
            v=input('Desea agregar otro artista: si/no ')
            if v =='si':
                continue
            else:
                print('Gracias ',spotify)
                break
        case 2:
            v=input('Ingresa el artista que desea buscar: ')
            if v in spotify:
                 buscarArts(spotify)
            else:
                q=input('Desea agregar un artista si/no')
                if q=='si':
                    artista(spotify)
                else:
                    print('Gracias por usar Spotify')
        case 3:
            buscarcancion(spotify)
        case 4:
            eliminar_artista(spotify)
        case 5:
            cancion_m(spotify)
        case 6:
            cancion_chiquita(spotify)
        case 7:
            ordenar(spotify)
        case _:
            print('Gracias por usar Spotify')