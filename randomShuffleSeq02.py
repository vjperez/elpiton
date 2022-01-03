import random
    
secuencia = ['uno', 'dos', 'tres', 'cuatro']

print('secuencia original')
for indice, valor in enumerate (secuencia):
    print(indice, ': ', valor)

random.shuffle(secuencia)
print('secuencia after using random.shuffle()....')
for indice, valor in enumerate (secuencia):
    print(indice, ': ', valor)