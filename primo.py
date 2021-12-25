#function works when n is an instance of int and n > 1
#by definition 1 is not prime, google it
def isPrimo(n):
	if isinstance(n, int) and n > 1:
		for isFactor in range(2,n):
			if n % isFactor == 0:
				return False
		return True
	else:
		raise Exception('n no es un numero entero mayor que 1.')
		



if __name__ == '__main__':
	n = 545		#hasta 231 to get 50 primes, hasta 545 ahi 100 primos
	cuantosPrimos = 0
	for n in range(2, n+1):
		if isPrimo(n):
			print(str(n) + ' es primo')
			cuantosPrimos += 1
		else:
			print('\t\t' + str(n) + ' no es primo')

	print('Desde 2, hasta', n, 'ahi', cuantosPrimos, 'primos.', sep=' ', end='\n\n')

	#exceptions
	#isPrimo(2.2)			este call, tambien tira exception
	isPrimo(1)