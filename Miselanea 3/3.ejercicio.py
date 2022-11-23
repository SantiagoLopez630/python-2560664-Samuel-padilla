import random
vec=[]
a=0
suma1=0
suma=0
cont1=1
prome1=0
for i in range(random.randint(10,25)):
    vec.insert(i,round(random.random()*100))
    suma+=vec[i]
    a+=1
    if i%2==0:
        print("El numero es par",vec[i])
    else:
        print("El numero es impar",vec[i])
        suma1+=vec[i]
        cont1=1
        prome1=suma1//cont1
print("El promedio de los impares es: ",prome1)
print(vec)
        

    