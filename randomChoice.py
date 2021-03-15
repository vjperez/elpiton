#a random choice of a sequence using choice( data ) from random

import random

#seq = [ x    for x in range(1,5)]
#seq = [ 1+x  for x in range(4)]
seq = [1, 2, 3, 4]
for i in range(20):
    print('random choice from 1 to 4: = ', random.choice( seq ))
print('\n\n')

# using randrange, to implement my version of choice
for i in range(20):
    print('random choice from  1 to 4 using randrange: = ', random.randrange(1,5))
print('\n\n')