#determines whether m is even; no int div or modulo
def par(m):
	if isinstance(m, int):
		m = -m if m < 0 else m 
		while m != 1 and m != 0:
			m -= 2
		if m == 0:	return True
		else:		return False	# m == 1
	else:
		raise TypeError('usa solo enteros...')
		

print(  '8 es par: ' + str(par(8))  )
print(  '9 es par: ' + str(par(9))  )
print(  '0 es par: ' + str(par(0))  )
print(  '1 es par: ' + str(par(1))  )
print()
print(  '9.3 es par: ' + str(par(9.3))  )