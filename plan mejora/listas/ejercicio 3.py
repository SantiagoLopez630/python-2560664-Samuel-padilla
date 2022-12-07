"""
Chatbot

python-Aprenda a programar proyectos lúdicos/Bucles, listas y entradas-salidas /proyectos
"""

import random 
 
Principio = [ "¿Cómo estás?" , "¿Por qué vienes a verme?", 
"¿Cómo te ha ido el día?"] 
 
IdenPADRE = [ " ¿Cómo está tu {0}?", "¿Tienes algún problema en la relación con tu {0}?", "¿Por qué estás pensando ahora en tu {0}?"] 
 
Preguntas = [ " ¿Por qué me haces esta pregunta?", 
"¿Harías esta pregunta a un humano?", "Desgraciadamente, no puedo responder a esa pregunta"] 
 
Superfluas= [ "Lo entiendo.", "Siento una pizca de arrepentimiento.", 
"¿Es una buena noticia?", "Sí, ese es el problema.", 
 "¿Piensas lo que estás diciendo?", "Ah… es posible."] 
 
k = random.randint(0,len(Principio)) 
print("@@ ",Principio[k]) 
 
for i in range(10): 
   frase = input() 
 
   # prueba de palabra clave 
 
   palabrasclave = ["padre","madre","amigo", "amiga", "mamá", "papá", "novio", "novia"] 
   found = "" 
   for palabrac in palabrasclave : 
      if frase.find(palabrac) > 0 : 
          found = palabrac 
 
   if len(found) > 0 : 
       k = random.randint(0,len(IdenPADRE)-1) 
       respuesta = IdenPADRE[k] 
       print("@@ ",respuesta.format(found)) 
 
   else : 
       # ¿es una pregunta? 
       
       if frase.find("?") > 0 : 
           k = random.randint(0,len(Preguntas)-1) 
           print("@@ ",Preguntas[k]) 
 
       else : 
           # rápido, una respuesta superflua: 
           k = random.randint(0,len(Superfluas)-1) 
           print("@@ ",Superfluas[k]) 
