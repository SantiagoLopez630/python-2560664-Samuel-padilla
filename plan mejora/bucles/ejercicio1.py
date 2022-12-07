"""
Resolver un criptoritmo

python-Aprenda a programar proyectos lúdicos/Bucles, listas y entradas-salidas /proyectos
"""

for D in range(1,10) : 
 for O in range(10) : 
  for S in range(10) : 
   for E in range(10) : 
    for I in range(10) : 
     for Z in range(10) : 
      dif1 = D != O and D != S and D != E and D != I and D!=Z 
      dif2 = O != S and O != E and O != I and O != Z 
      dif3 = S != E and S != I and S != Z 
      dif4 = E != I and E != Z and I != Z 
      if dif1 and dif2 and dif3 and dif4 : 
       DIEZ = D * 1000 + I * 100 + E * 10 + Z 
       DOS= D * 100 + O * 10 + S 
       SEIS = S * 1000 + E * 100 + I * 10 + S 
       if DOS + DOS + SEIS == DIEZ : 
         print(DOS,"+",DOS,"+",SEIS,"=",DIEZ )