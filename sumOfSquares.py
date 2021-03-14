#sum of squares of integers from zero to n

n= int(input('n= '))
n = (n if n>=0 else -n)

#method 1
suma1 = 0
for j in range(1, n):
    suma1 = suma1 + j*j

#method 2
listaDeCuadrados = [k*k for k in range(1,n)]
suma2 = 0
for l in listaDeCuadrados:
    suma2 = suma2 + l

#method 3
suma3 = sum( [k*k for k in range(1,n)] )

print('Suma de cuadrados desde cero hasta ' , n, ' es ', suma1, '\n2do metodo: ', suma2, '\n3er metodo: ', suma3)