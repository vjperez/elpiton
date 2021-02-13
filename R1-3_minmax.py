# input: sequence of 1 or more numbers 
# output: tuple containing min and max

def minmax(seq):
	if isinstance(seq, list):
		if len(seq) == 0: 
			return (None, None)
		else:
			min, max = seq[0], seq[0]
			for index in range(1, len(seq)):
				if   seq[index] > max:	max = seq[index]
				elif seq[index] < min:	min = seq[index]
			return (min, max)
	else:
		raise TypeError('input debe ser tipo list...')
		
lista = [199, 2, -11, 17, -3]
min, max = minmax(lista)
print('lista: ' , lista[0:len(lista)] , '\tmin: ' , min , '\tmax: ' , max , '\n\n')

lista = [99]
min, max = minmax(lista)
print('lista: ' , lista , '\tmin: ' , min , '\tmax: ' , max , '\n\n')

lista = []
min, max = minmax(lista)
print('lista: ' , lista[0:len(lista)] , '\tmin: ' , min , '\tmax: ' , max , '\n\n')

lista = {8}
min, max = minmax(lista)
print('lista: ' , lista[0:len(lista)] , '\tmin: ' , min , '\tmax: ' , max , '\n\n')