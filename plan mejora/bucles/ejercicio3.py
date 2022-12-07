"""
Hacer un programa que permita ingresar dos numeros al usuario, le saque el cuadrado y luego los compare
"""

num1, num2 = input("ingrese los numeros que desea operar separados por un espacio ").split()
num1 = int(num1)
num2 = int(num2)
num1 = pow(num1, 2)

while num1 and num2 > 0 :
       if num2==num1:
              print("El segundo es el cuadrado exacto del primero")
       elif num2<num1:
              print("El segundo es menor que el cuadrado del primero") 
       elif num2>num1:
              print("El segundo es mayor que el cuadrado del primero") 
       else:
              print("Syntax error") 
       break