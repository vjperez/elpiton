size = 10
for n in range( 1, size + 1 ):
	if n % 2 == 0 and n % 3 == 0:
		print(str(n) + ': six pack')
	elif n % 2 == 0:
		print (str(n) + ': par')
	elif n % 3 == 0:
		print(str(n) + ': trio')
	else:
		print(n)
		