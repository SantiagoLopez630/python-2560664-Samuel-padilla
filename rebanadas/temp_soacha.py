import random 

tam=round(random.randint(7,19))
vec=[]
suma1=0
suma2=0
suma3=0
print('Tamaño',tam)

for i in range(tam) :
    vec.append(round(random.randint(7,19)))
print(vec)

mitad1=vec[:(tam//2)]
print(mitad1)
for i in mitad1:
    suma1+=i
promedio1=suma1/len(mitad1)
print(promedio1)    
mitad2=vec[(tam//2):]
print(mitad2)
for i in mitad2:
    suma2+=i
promedio2=suma2/len(mitad2)    
print(promedio2)
tercio1=vec[(tam*(1/3)):]
print(tercio1)
for i in tercio1:
    suma3+=i
promedio3=suma3/len(tercio1)    
print(promedio3)