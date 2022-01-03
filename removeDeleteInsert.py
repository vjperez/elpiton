import printeaSeq, random

lista = ['Victor', 'rosa', 'rosa', 'diego', 'viso', 'rosa', 'rosa', 'rosa']
printeaSeq.printeaSeq('lista original', lista)
print()

del lista[0]
printeaSeq.printeaSeq('lista after removing index 0 ', lista)
print()

lista.remove('rosa')
printeaSeq.printeaSeq('lista after removing "rosa"', lista)
print()

lista.insert(0, 'rosa')
printeaSeq.printeaSeq('reinserting rosa at zero', lista)
print()

lista.remove( lista[4] )
printeaSeq.printeaSeq('removing first item with same value as index 4, (rosa)...', lista)
print()

lista.remove( lista[-1+len(lista)] )
printeaSeq.printeaSeq('removing first item with same value as last,  (rosa)...', lista)
print()