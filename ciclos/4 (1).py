for num in range (1,1001):
  suma = 0
  
  for i in range (1,num):

    if (num % i == 0):

      suma += i

  if num == suma:

    print('El numero', num, 'es perfecto ;)')

  else:

    print('El numero', num, ' NO es perfecto :(')
 