lista = ['victor', 'rosa', 'diego', 'viso']

for indice, valor in enumerate (lista):
    print('el indice', indice, 'contiene', valor)


print('\n', 'same as..', '\n')

for indice in range( len(lista) ):
    print('el indice', indice, 'contiene', lista[indice])