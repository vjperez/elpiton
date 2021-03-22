import printeaSeq

# creating list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
# el numero anterior es  i(i-1) y para llegar al numero i, se le suma 2*i
# i(i-1) + 2i = i^2 + i
lista = [ i + i*i for i in range(10)]

printeaSeq.printeaSeq('lista', lista)