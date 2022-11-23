"""
Los numeros que se guardan en una vector son edades y en cada espacio debe decir si es menor o mayor de edad 
"""
import random 

vector=[round(random.random()*100) for i in range(10)]
print(vector)
edad= ['Mayor' if x>=18 else 'Menor' for x in vector]
print(edad)
