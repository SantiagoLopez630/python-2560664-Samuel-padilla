import random
vec=[]
a=0
suma=0
for i in range(random.randint(10,25)):
    vec.insert(i,round(random.random()*100))
    suma+=vec[i]
    a+=1
    promedio=suma//a

    if i < promedio:
        print("El numero esta por debajo del promedio",vec[i])
    elif i == promedio:
        print("El numero es igual al promedio",vec[i])
    else:
        print("El numero esta por encima del promedio",vec[i])
print(vec)