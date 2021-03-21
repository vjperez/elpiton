import printeaSeq

# mutar la seq sumando 1 a los items, 
# usando diferentes loops

def addOneVersion1(seq):
    for item in seq:
        item = item + 1

def addOneVersion2(seq):
    for item in seq:
        item += 1

def addOneVersion3(seq):
    for index in range(len(seq)):
        seq[index] = seq[index] + 1

def addOneVersion4(seq):
    for index in range(len(seq)):
        seq[index] += 1



# testing muting functions
seq = [2, 8, 16]
printeaSeq.printeaSeq('original seq', seq)

addOneVersion1(seq)
printeaSeq.printeaSeq('after version 1 was called', seq)

addOneVersion2(seq)
printeaSeq.printeaSeq('after version 2 was called', seq)

addOneVersion3(seq)
printeaSeq.printeaSeq('after version 3 was called', seq)

addOneVersion4(seq)
printeaSeq.printeaSeq('after version 4 was called', seq)