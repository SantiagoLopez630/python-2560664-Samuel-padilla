"""
Una tienda vende diferentes productos, usualmente frutas, dulces y algunos tipos de carne. Con el propósito de mejorar el control sobre las ventas y el inventario de la tienda, el gerente decide construir una aplicación que le permita almacenar la información de los productos y realizar algunos cálculos sobre los datos.

En la primera parte del reto se debe construir una base de datos que almacene la información de los productos disponibles en la tienda. La base de datos será representada mediante un diccionario de Python llamado productos que tendrá por llave el código del producto y por valor una lista formada por los atributos: nombre, precio e inventario. La Tabla 1 presenta los productos disponibles a la fecha.
"""
def leer_datos():
    operacion = input()
    producto = input().split()
    producto[0] = int(producto[0])
    producto[2] = float(producto[2])
    producto[3]= int(producto[3])    
    return operacion, producto
    
def agregar(creacionbaseDatos, producto):
    if producto[0] in creacionbaseDatos:
        return False
    index = producto[0]
    producto.pop (0)
    creacionbaseDatos[index] = producto
    return True    

def actualizar(creacionbaseDatos, producto):
    if producto[0] in creacionbaseDatos:
        index = producto [0]
        producto.pop(0)
        creacionbaseDatos[index] = producto
        return True
    return False
                
def borrar(creacionbaseDatos, producto):
    if producto[0] in creacionbaseDatos:
       creacionbaseDatos.pop(producto[0])
       return True
    return False         
 
def preciomayor(creacionbaseDatos):
    mayor = list(creacionbaseDatos.keys())[0]
    for i in creacionbaseDatos:
        if creacionbaseDatos[i][1] > creacionbaseDatos[mayor][1]:
            mayor = i
    return creacionbaseDatos[mayor][0]
       
def preciomenor(creacionbaseDatos):
    menor = list(creacionbaseDatos.keys())[0]
    for i in creacionbaseDatos:
        if creacionbaseDatos[i][1] < creacionbaseDatos[menor][1]:
            menor = i
    return creacionbaseDatos[menor][0]

def promedio_precios(creacionbaseDatos):
    promedio = 0
    for i in creacionbaseDatos:
        promedio += creacionbaseDatos[i][1]
    promedio /= len(creacionbaseDatos)
    return promedio

def valor_inventario(creacionbaseDatos):
    valor_inventario = 0.0
    for i in creacionbaseDatos:
        valor_inventario += creacionbaseDatos[i][1] * creacionbaseDatos[i][2]
    return valor_inventario
 
creacionbaseDatos = {
    1:	["Manzanas"  , 5000.0,25],
    2:	["Limones"   , 2300.0,15],
    3:	["Peras"     , 2700.0,33],
    4:	["Arandanos" , 9300.0,5],
    5:	["Tomates"   , 2100.0,42],
    6:	["Fresas"    , 4100.0,3],
    7:	["Helado"    , 4500.0,41],
    8:	["Galletas"  , 500.0,8],
    9:	["Chocolates", 3500.0,80],
    10: ["Jamon"     , 15000.0,10],
}
operacion, producto = leer_datos()
    
if operacion == "AGREGAR" :
    flag = agregar(creacionbaseDatos, producto)
elif operacion == "ACTUALIZAR" :
    flag = actualizar(creacionbaseDatos, producto)
elif operacion == "BORRAR" :
    flag = borrar(creacionbaseDatos, producto)
if flag:
  print(preciomayor(creacionbaseDatos),preciomenor(creacionbaseDatos),round(promedio_precios(creacionbaseDatos),1),
        round(valor_inventario(creacionbaseDatos),1))
else:
  print('ERROR')