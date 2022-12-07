"""
python 3, curso practico pag 290
"""

def elevar_2(numero: int , lista = [1, 2, 3]):
    print('La variable antes de ejecutar la función es: ', lista)
    for i in range(0, len(lista)):
        lista[i] = lista[i] **2
    numero = numero**2

    return lista, numero

def main():
    numero = 10

    print('la variable numero antes de ejecutar la función es: ', numero)
    lista, numero = elevar_2(numero)
    print('la variable numero despues de ejecutar la función es: ', numero)
    print('la variable lista despues de ejecutar la función es: ', lista,'\n')

    print('la variable numero antes de ejecutar la función es: ', numero)
    lista, numero = elevar_2(numero)
    print('la variable numero despues de ejecutar la función es: ', numero)
    print('la variable lista despues de ejecutar la función es: ', lista,'\n')

    print('la variable numero antes de ejecutar la función es: ', numero)
    lista, numero = elevar_2(numero,[5, 5, 5, 5, 5])
    print('la variable numero despues de ejecutar la función es: ', numero)
    print('la variable lista despues de ejecutar la función es: ', lista,'\n')

main()