#determines whether m is a multiple of n
# i * n = m for any integer i  
def multiplo(m, n):
	if isinstance(m, int) and isinstance(n, int):
		if m == 0: 
			return True
		elif n == 0:
			return False
		else:
			return m % n == 0
	else:
		raise TypeError('usa solo enteros...')
		

print(  '8 es multiplo de 2: ' + str(multiplo(8, 2))  )
print(  '11 es multiplo de 2: ' + str(multiplo(11, 2))  )
print(  '0 es multiplo de 3: ' + str(multiplo(0, 3))  + '  Cero es multilo de todo entero ?!'  )
print(  '7 es multiplo de 0: ' + str(multiplo(7, 0))  + '  Ningun entero es multiplo de cero ?!'  )
print(  '0 es multiplo de 0: ' + str(multiplo(0, 0))  + '  Excepto cero, q si es multiplo de cero ?!'  )
print()
print(  '11.9 es multiplo de 2: ' + str(multiplo(11.9, 2))  )