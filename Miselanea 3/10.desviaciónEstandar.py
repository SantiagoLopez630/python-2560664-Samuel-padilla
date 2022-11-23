import random 

tam=round(random.randint(5,10))
vec=[]
dif=[]
media= 0
print('Tamaño',tam)

for i in range(tam) :
    vec.append(round(random.random()*100))
print(vec)

for i in vec :
    media+=i
media=media/len(vec)
print('Media', media)
suma= 0
for i in range(len(vec)):
    x=(vec[i]-media)**2
    dif.append(x)
    suma+=x
print('Suma', suma)
print('desviación estandar', (suma/len(vec))**0.5)