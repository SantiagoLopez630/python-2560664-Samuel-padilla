supermercado = {}

while True:
    producto = input("Ingresa el producto: ")
    if producto == '':
        break
    
    precio = int(input("Ingresa el precio del producto: "))
    if precio<0:
        break

    if producto in supermercado:
        supermercado[producto] += (precio,)
    else:
        supermercado[producto] = (precio,)
        
for producto in sorted(supermercado.keys()):
    adding = 0
    counter = 0
    for score in supermercado[producto]:
        adding += score
        counter += adding
    print(producto, ":", adding)
    
print('El precio total a pagar es', counter)