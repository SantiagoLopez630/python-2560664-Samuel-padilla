"""
Elaborar un programa que muestre cuantos datos desee un usuario, de la serie fibonachi
"""
n1=0
n2=1
nDatos=int(input("ingrese el numero de datos que desea"))
contador=0
print(n1)
print(n2)
while contador<nDatos-2:
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
    contador=contador+1