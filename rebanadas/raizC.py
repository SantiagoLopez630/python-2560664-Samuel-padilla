import random 

tam=round(random.randint(7,19))

vec=[(i+1)**0.5 for i in range(tam)]
print(vec)

vector=[round(random.random()*100) for i in range(10)]
print(vector)
pares=[x for x in vector if x%2==0]
impares=[x for x in vector if x%2!=0]
print(pares)
print(impares)


impares2=[]
pares2= [x if x %2==0 else impares2.append(x) for x in vector]
print(pares2)
print(impares2)

