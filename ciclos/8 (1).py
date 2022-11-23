def multiplo(valor, multiplo):

    """

    Funcion para calcular si el numero es multiplo

    utilizando el modulo de la division

    """

    return True if valor % multiplo == 0 else False

 

# lista que contendra los valores multiples


multiplos_5=[]

 

# bucle del 1 al 100

for i in range(1, 101):

    if multiplo(i, 5):

        multiplos_5.append(i)


print ("\nLos multiplos de 5 son:", multiplos_5)