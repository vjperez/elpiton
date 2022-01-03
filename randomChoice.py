#a random choice of a list using choice( data ) from random

import random

lista = ['victor', 'rosa', 'diego', 'viso']

for i in range(200):
    print('random choice from lista: = ', random.choice( lista ))
print('\n\n')

# using randrange, to implement my version of choice, rand range allows for a start, stop, and a step
for i in range(200):
    indiceRandom = random.randrange( len(lista) )
    print('random choice from  lista using randrange: = ', lista[indiceRandom])
print('\n\n')


# using randint, to implement yet another version of choice
for i in range(200):
    indiceRandom = random.randint(0, -1 + len(lista) )
    print('random choice from  lista using randint: = ', lista[indiceRandom])
print('\n\n')