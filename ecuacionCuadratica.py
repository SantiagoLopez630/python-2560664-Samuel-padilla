from math import sqrt 

a, b, c = input("ingrese los numeros que desea operar separados por un espacio ").split()
a = int(a)
b = int(b)
c = int(c)


x_1 = -b + sqrt(b**2 - 4*a*c) / (2*a)
x_2 = -b - sqrt(b**2 - 4*a*c) / (2*a)

print('El valor positivo de la ecuación es', x_1)
print('El valor negativo de la ecuación es', x_2)

