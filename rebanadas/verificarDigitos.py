"""
De los diez numeros que genera con random los demas numeros rellene con 0
"""
import random 

vector=[round(random.random()*100) for i in range(10)]
print(vector)
impares2=[]
digitos= [x if x/100<=0.09 else 0 for x in vector]
print(digitos)


