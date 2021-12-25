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
		

n = 20
for n in range(2, n+1):
	if primo(n):
		print(str(n) + ' es primo')
	else:
		print('\t\t' + str(n) + ' no es primo')
		
#primo(2.2)			este call, tambien tira exception
primo(0)