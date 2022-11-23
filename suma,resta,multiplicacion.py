
def sumar_fracciones(fracciones):
    suma = 0

    for f in fracciones:
        suma += f[0]/f[1]
    
    return round(suma)

def restar_fracciones(fracciones):
    resta = 0

    for f in fracciones:
        resta -= f[0]/f[1]
    
    return round(resta)

def multiplicar_fracciones(fracciones):
    multi = 0

    for f in fracciones:
        multi *= f[0]/f[1]
    
    return round(multi)

def dividir_fracciones(fracciones):
    divi = 0

    for f in fracciones:
        divi /= f[0]/f[1]
    
    return round(divi)
numeros = [(2, 3), (1, 2), (3, 2), (1, 3)]
resultado = sumar_fracciones(numeros)
resultado1 = restar_fracciones(numeros)
resultado2= multiplicar_fracciones(numeros)
resultado3= dividir_fracciones(numeros)
print(resultado)
print(resultado1)
print(resultado2)
print(resultado3)