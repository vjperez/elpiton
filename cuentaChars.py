import pprint

texto = 'Victor es calvo y gordito.'

cuenta = {}
for letra in texto:
    cuenta.setdefault(letra, 0)
    cuenta[letra] += 1 


print('\nCounting chars on:...', texto)
pprint.pprint(cuenta)

print('\n', texto, cuenta, '\n', sep='\n')