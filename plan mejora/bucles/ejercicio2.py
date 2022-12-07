"""
 El juego del tres en raya 

python-Aprenda a programar proyectos lúdicos/Bucles, funciones /proyectos
"""

from tkinter import Tk, Canvas 
import random 
 
TAMANO = 300 
JUEGO = [ [0,0,0],[0,0,0],[0,0,0]] 
 
def MostrarCuadricula(c="black"): 
  canvas.create_line((100,0),(100,300),width=3,fill=c) 
  canvas.create_line((200,0),(200,300),width=3,fill=c) 
  canvas.create_line((0,100),(300,100),width=3,fill=c) 
  canvas.create_line((0,200),(300,200),width=3,fill=c) 
 
def MostrarFichas(): 
  for x in range(3): 
     for y in range(3): 
        xx = x * 100 
        yy = y * 100 
        A = (xx+20,yy+20) 
        B = (xx+80,yy+80) 
        C = (xx+20,yy+80) 
        D = (xx+80,yy+20) 
        if JUEGO[x][y] == 1 : 
           canvas.create_oval(A,B,fill="blue") 
        if JUEGO[x][y] == 2 : 
           canvas.create_line(A,B,fill="red",width=10) 
           canvas.create_line(C,D,fill="red",width=10) 
 
def DetectarVictoria(): 
  for j in [1,2] : 
     for x in range(3): 
        if JUEGO[x][0] == JUEGO[x][1] == JUEGO[x][2] == j : return j 
     for y in range(3): 
        if JUEGO[0][y] == JUEGO[1][y] == JUEGO[2][y] == j : return j 
     if JUEGO[0][0] == JUEGO[1][1] == JUEGO[2][2] == j : return j 
     if JUEGO[0][2] == JUEGO[1][1] == JUEGO[2][0] == j : return j 
  return 0 
 
def BuscarCasillaVacia() : 
  L = [] 
  for x in range(3): 
     for y in range(3): 
        if JUEGO[x][y] == 0 : 
           L.append((x,y)) 
  if len(L) == 0 : return False 
  else : 
     i = random.randint(0,len(L)-1) 
     return L[i] 
 
def PROG() : 
  MostrarCuadricula() 
 
def Mostrar(): 
  canvas.delete("all") 
  MostrarCuadricula() 
  MostrarFichas() 
 
def clic(event): 
  global JUEGO 
  Mostrar() 
  x = event.x // 100 
  y = event.y // 100 
 
  if DetectarVictoria() != 0 : # reinicia una partida 
     JUEGO = [ [0,0,0],[0,0,0],[0,0,0]] 
     Mostrar() 
     return 
 
  if JUEGO[x][y] != 0 : return # clic en una zona donde ya se ha jugado 
 
  # JUGADOR HUMANO 
  JUEGO[x][y] = 1 
  MostrarFichas() 
  if DetectarVictoria() == 1 : 
     MostrarCuadricula("blue") 
     return 
 
  # JUGADOR COMPUTADORA 
  calculo = BuscarCasillaVacia() 
  if calculo != False : 
     x,y = calculo 
     JUEGO[x][y] = 2 
     MostrarFichas() 
     if DetectarVictoria() == 2: 
       MostrarCuadricula("red") 
       return 
 
# Creación de la ventana gráfica 
Miventana = Tk() 
Miventana.geometry(str(TAMANO) +"x"+str(TAMANO)) 
canvas = Canvas(Miventana,width=TAMANO, height=TAMANO, 
borderwidth=0, highlightthickness=0,bg="lightgray") 
canvas.pack() 
Miventana.after(100,PROG) 
Miventana.bind("<Button-1>", clic)  #añadir esta línea 
Miventana.mainloop() 