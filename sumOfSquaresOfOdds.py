#sum of squares of odd integers, from zero to BEFORE n

n= int(input('n= '))
n = (n if n>=0 else -n)

#method 1
suma1 = 0
for j in range(1, n, 2):
    suma1 = suma1 + j*j

#method 2
listaDeCuadrados = [k*k for k in range(1,n) if(k%2 == 1)]
suma2 = 0
for l in listaDeCuadrados:
    suma2 = suma2 + l

#method 3
suma3 = sum( [k*k for k in range(1,n) if(k%2 == 1)] )

print('Suma de cuadrados de impares, desde cero hasta antes de ' , n, ' es ', suma1, '\n2do metodo: ', suma2, '\n3er metodo: ', suma3)