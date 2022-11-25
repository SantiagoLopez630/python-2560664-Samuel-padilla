from math import sqrt 

a, b, c = input("ingrese los numeros que desea operar separados por una coma ").split(",")
a = int(a)
b = int(b)
c = int(c)

def resolver(a,b,c):
   
    try:
        x1 = -b + sqrt(b**2 - 4*a*c) / (2*a)
        x2 = -b - sqrt(b**2 - 4*a*c) / (2*a)
        resultado={
            'positivo': round(x1),
            'negativo': round(x2)
        }
        print(resultado)
    except ValueError:
        print('NO se puede hallar la raiz de un numero negativo')
    except ZeroDivisionError:
        print('La división no se puede ejecutar por cero')
    except: 
        print('syntax error')

resolver(a,b,c)