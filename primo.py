#function works when n is an instance of int and n > 1
#by definition 1 is not prime, google it
def primo(n):
	if isinstance(n, int) and n > 1:
		for isFactor in range(2,n):
			if n % isFactor == 0:
				return False
		return True
	else:
		raise Exception('n no es un numero entero mayor que 1.')
		

n = 231
cuantosPrimos = 0
for n in range(2, n+1):
	if primo(n):
		print(str(n) + ' es primo')
		cuantosPrimos += 1
	else:
		print('\t\t' + str(n) + ' no es primo')

print('Desde 2, hasta', n, 'ahi', cuantosPrimos, 'primos.', sep=' ', end='\n\n')

# exceptions
#primo(2.2)			este call, tambien tira exception
primo(1)