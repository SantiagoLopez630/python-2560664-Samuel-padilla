"""
Almacenar los datos de ventas de tres comerciales, tenemos tres posibles articulos a lo largo de tres posibles meses.
Por lo tanto tendriamos tres comerciales, tres meses y tres articulos. Podemos crear una lista donde sus elementos
sean listas cuyos elementos a su vez sean listas de tres elementos, que serán los datos de venta

python 3: curso practico pag 308
"""



import random

datos = []

for i in range(3):
    datos.append([])
    for j in range(3):
        datos[i].append([])
        for k in range(3):
            datos[i][j].append(random.randint(0,50))

print(datos)

for i in range(3):
    for j in range(3):
        for l in range(3):
            print('las ventas del comercial', i+1,\
                'en el mes', j+1, 'del articulo',\
                k+1, 'han sido', datos[i][j][k])

print('\n los datos completos del comercial 1 son:', datos[0])
print('los datos completos del comercial 1 en el mes 1 son:', datos[0][0])
print('El datos de ventas del comercial 1 en el mes 1 del articulo 1 son:', datos[0][0][0])
