def dias():
    dia=int(input('Ingrese el numero del dia de la semana: '))    

    if dia==1:
        print('Lunes')
    elif dia==2:
        print('Martes')
    elif dia==3:
        print('Miercoles')
    elif dia==4:
        print('Jueves')
    elif dia==5:
        print('Viernes')
    elif dia==6:
        print('Sabado')
    elif dia==7:
        print('Domingo')

    return dia

def validarDia():
    try:
        dias()
    except TypeError: 
        print('Ingrese un numero de 1 a 7')
    except ValueError:
        print('Solo se admiten numeros')

validarDia()