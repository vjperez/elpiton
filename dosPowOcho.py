#dos a la ocho 
#use list comprehension to produce list = [1, 2, 4, 8, 16, 32, 64, 128, 256]

print('a list from 2^0 to 2^8')
print('Using list comprehension to produce list = [1, 2, 4, 8, 16, 32, 64, 128, 256]')

lista = [ pow(2, x) for x in range(9)]
print('lista=', end='  ')
for value in lista:
    print(value, end=', ')
print(end='\n\n')