"""
Ejercicio 2
En una curva peligrosa, con limite de velocidad a 40 kilómetros/hora, circula un coche a 36 kilómetros/hora.
Otro, de la misma masa, 2000 kg, no respeta la señal y marcha a 72 kilómetros/hora

¿Qué energia cinetica posee cada uno?
"""

import math
def calcularEjercicio():
    print('Ejercicio 2\n En una curva peligrosa, con limite de velocidad a 40 kilómetros/hora, circula un coche a 36 kilómetros/hora.\n Otro, de la misma masa, 2000 kg, no respeta la señal y marcha a 72 kilómetros/hora \n ¿Qué energia cinetica posee cada uno?\n')
    rta,rta2=int(input('Ingrese la energia del carro 1 y carro 2 respectivamente separados por coma')).split(",")
    rta=int(rta)
    rta2=int(rta2)
    #conversión unidades
    va= (36*1000)//3600
    vb= (72*1000)//3600
    #calcular velocidades
    Eca= int((1/2)*2000 *(10^2))
    Ecb= int((1/2)*2000 *(20^2))

    if Eca and Ecb == rta and rta2:
        print('Muy bien :), has acertado. La respuesta correcta es ',Eca,Ecb)
    elif Eca == rta :
        intento=input('Vaya :/, solo has hacertado en la primera',Eca,'Deseas volver a intentarlo? s/n \n')
        if intento == 's' :
            try :
                calcularEjercicio()
            except ValueError:
                print('Solo se aceptan valores numericos')
            except :
                print('error')
    elif Ecb == rta2 :
        intento=input('Vaya :/, solo has hacertado en la primera',Ecb,'Deseas volver a intentarlo? s/n \n')
        if intento == 's' :
            try :
                calcularEjercicio()
            except ValueError:
                print('Solo se aceptan valores numericos')
            except :
                print('error')
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