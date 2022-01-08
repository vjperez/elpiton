import printeaSeq

texto = 'Victor es calvo y gordito.'

cuenta = {}
for letra in texto:
    cuenta.setdefault(letra, 0)
    cuenta[letra] += 1 


print(texto, cuenta, sep='\n')