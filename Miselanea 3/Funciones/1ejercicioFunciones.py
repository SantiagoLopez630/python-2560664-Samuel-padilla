import random
tam=round(random.randint(10,25))
def llenar(vec):

    for i in range(tam):
        vec.insert(i,round(random.random()*100))
    return vec

def promediar(vec):
    a=0
    suma=0
    for i in range(tam):
        suma+=vec[i]
        a+=1
        promedio=suma//a
        if i < promedio:
            return "El numero esta por debajo del promedio",vec[i]
        elif i == promedio:
            return "El numero es igual al promedio",vec[i]
        else:
            return"El numero esta por encima del promedio",vec[i]

vector=[]
vector=llenar(vector)
print(vector)
msj=promediar(vector)
print(msj)
