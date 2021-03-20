#reverse a sequence

seq = ['a', 2, 3, 4, 'e'] 
print('sequence original..')
for item in seq:
    print(item, ' ', sep='', end='')
print('\n\n')

print('reversed seq..')
for i in range( -1 + len(seq), -1, -1):
    print( seq[i], ', ', sep='', end='') if i > 0 else print(seq[i])
print('\n\n')