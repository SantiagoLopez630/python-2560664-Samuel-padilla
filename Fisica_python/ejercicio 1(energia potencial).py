"""
Ejercicio 1
Subimos un objeto de 12Kg y lo subimos por una rampa inclinada 30º una distancia de 14 metros.

¿Qué energía potencial tendrá al llegar arriba?
"""

import math
def calcularEjercicio():
    print('Ejercicio 1 \n Subimos un objeto de 12Kg y lo subimos por una rampa inclinada 30º una distancia de 14 metros. \n ¿Qué energía potencial tendrá al llegar arriba?\n')
    rta=int(input('Ingrese la respuesta al problema '))
    rad= 30*180/math.pi
    sen= math.sin(rad)
    d=14
    h=d*sen
    Ep=int(round(12*(9.8)*7))

    if Ep== rta:
        print('Muy bien :), has acertado. La respuesta correcta es ',Ep)
    else :
        intento=input('La respuesta es incorrecta :( . Desea volver a intertarlo? s/n \n')
        if intento == 's' :
            try :
                calcularEjercicio()
            except ValueError:
                print('Solo se aceptan valores numericos')
            except :
                print('error')

try :
    calcularEjercicio()
except ValueError:
    print('Solo se aceptan valores numericos')
except :
    print('error')