"""
Calcular el número Pi

python-Aprenda a programar proyectos lúdicos/Bucles, listas y entradas-salidas /proyectos
"""

import math 
 
for k in range(3) : 
 n = 16 * 10**k 
 print("n =",n) 
 recuento = 0 
 ancho_casilla = 2 / n 
 for y in range(n): 
   for x in range(n): 
     xx = ancho_casilla * x 
     yy = ancho_casilla * y 
     dx = xx - 1 
     dy = yy - 1 
     d2 = dx*dx + dy*dy 
     if d2 < 1 :  # equivale a math.sqrt(d2) < 1 
       recuento += 1 
 
 aprox_pi = 4 * recuento / (n*n) 
 print("Aproximación de pi: " , aprox_pi) 
 error = abs(aprox_pi-math.pi) 
 error_teorico = 16 / n 
 print("Error estimación   : ", error) 
 print("Error teórico      : ", error_teorico) 
 print() 