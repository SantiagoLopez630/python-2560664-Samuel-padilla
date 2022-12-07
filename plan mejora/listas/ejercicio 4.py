"""
Una de las fortalezas deportivas que tiene Colombia y que más glorias le ha dado al país es el ciclismo. 
En Colombia las dificultades de la topografía han forjado a nuestros escarabajos que entrenaban en arcaicas bicicletas. La competencia internacional implica competir sobre bicicletas que día a día tienen más tecnología y menos peso. 
En las competencias se definen por reglamento las dimensiones de las bicicletas, las cuales se espera que unifiquen las condiciones de los ciclistas. La Unión de Ciclismo Internacional (UCI) define un reglamento técnico en el cual se encuentran las especificaciones de la bicicleta. 
Sin embargo, la mayoría de diseños suelen establecer algunos detalles por fuera de las medidas reglamentarias.

"""

def llenarBD(num):
    bicicletas= []
    contador = 1
    while (contador <= num):
        cadena = input().split()
        bicicletas.append(cadena)
        contador = contador + 1
    return bicicletas


def validarData(datos):
    valida = False
    precios= []
    for i in datos:
        if int(i[0])>= 240 and int(i[0])<= 300 \
            and int(i[1])>=160 and int(i[1])<=180 \
            and int(i[2])>=240 and int(i[2])<=275 \
            and int(i[3])<=50:
                valida = True
                precios.append(int(i[4]))
    if valida == True:
        return precios
    else: 
        return ["NO DISPONIBLE"]

n = int(input())
data = llenarBD(n)
respuesta = validarData(data)
for i in respuesta:
    print(i)