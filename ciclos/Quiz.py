"""
Solicite N al usuario de los numeros de 1 a 1000. Cuantos son multiplos de N? Ademas sumelos y promedielos 

"""

N=int(input('Ingrese un numero '))

for i in range (1,1001):
    suma=0
    if i%N == 0 :
        print(i)
        suma= suma+i
suma= suma+i

print(suma)
