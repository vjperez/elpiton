#a random choice of a sequence using choice( data ) from random

import random

seq = [101, 200, 333, 407]

for i in range(20):
    print('random choice from seq: = ', random.choice( seq ))
print('\n\n')

# using randrange, to implement my version of choice
for i in range(20):
    indiceRandom = random.randrange(4)
    print('random choice from  seq using randrange: = ', seq[indiceRandom])
print('\n\n')