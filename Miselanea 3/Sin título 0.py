# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 16:48:41 2022

@author: Aprendiz
"""

import random 


cont=0
cont1=0
suma=0
suma1=0
tam=int(input('Ingrese cantidad '))
vec=[]
for i in range(tam):
    vec.insert(i,round(random.random()*100))
print(vec)

for i in range(len(vec)):
    if vec[i]%2==0:
        print(vec[i],' es un numero par')
        cont=cont+1
        suma=suma+vec[i]
        prome=suma/cont
    else:
        print(vec[i],' es un numero impar')
        cont1=cont1+1
        suma1=suma1+vec[i]
        prome1=suma1/cont1
        