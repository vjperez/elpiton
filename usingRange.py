#using range

print('Usando range con prototipo, range(50, 90, 10) debe producir 50, 60, 70, 80 ...')
seq = range(50, 90, 10)
print('secuencia:', end=' ')
for value in seq:
    print(value, end= '  ')
print(end='\n\n')

print('Usando range con prototipo, range(8, -10, -2) debe producir 8, 6, 4, 2, ... -4, -6, -8')
seq = range(8, -10, -2)
print('secuencia:', end=' ')
for value in seq:
    print(value, end= '  ')
print(end='\n\n')


print('Printing seq directo con str')
print( str(seq) )