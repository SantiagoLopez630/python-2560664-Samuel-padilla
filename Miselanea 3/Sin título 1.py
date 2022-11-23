# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 17:29:06 2022

@author: Aprendiz
"""

import random 


cont=0
cont1=0
suma=0
suma1=0
tam=random.randint(10, 25)
mediana=tam/2
vec=[]
for i in range(tam):
    vec.insert(i,round(random.randint(0, 100)))
    mediana=vec[mediana]
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
        
        