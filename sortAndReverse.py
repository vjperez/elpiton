import printeaSeq, random

lista = ['Victor', 'rosa', 'diego', 'viso']
printeaSeq.printeaSeq('lista original', lista)

lista.sort()
printeaSeq.printeaSeq('lista sorteada (based on ASCII values upper goes first)', lista)

lista.sort(key=str.lower)
printeaSeq.printeaSeq('lista sorteada (based on alphabetical values, case dont matter)', lista)

random.shuffle(lista)
printeaSeq.printeaSeq('lista shuffled...', lista)

lista.reverse()
printeaSeq.printeaSeq('lista al reves...', lista)

random.shuffle(lista)
printeaSeq.printeaSeq('lista shuffled...', lista)

lista.sort(key=str.lower)
lista.reverse()
printeaSeq.printeaSeq('lista sorteada y al reves ...', lista)