dict={
    'gato' : 'cat',
    'caballo' : 'horse',
    'vaca' : 'cow',
    'hormiga' : 'ant',
    'perro' : 'dog'

}

print(dict)
print(dict.get('perro'))
print(dict['vaca'])

del dict['perro']
print(dict)

dict['raton']= 'mouse'
print(dict)

dict.update({'perro':'dog'})
print(dict)

dict.popitem()
print(dict)

for i in dict.keys():
    print(i)

for i in dict.values():
    print(i)

for i in dict.items():
    print(i)

print(sorted(dict.items()))