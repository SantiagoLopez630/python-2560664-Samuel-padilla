import random
valor=[round(random.random()*100) for i in range(random.randint(10,25))]
a=0
suma=0
for i in range(len(valor)):
    suma+=valor[i]
    a+=1
    promedio=suma//a
res=['Debajo promedio' if valor<promedio else 'encima promedio' for i in valor]
print(promedio)
print(valor)

