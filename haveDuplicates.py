# duplicates on a numbers sequence ?
# as soon as equals elements are found, True is retuned, 
# Empty sequences and sequences with only 1 element will receive False as result
def haveDuplicates(seq):
    for index01 in range(-1 + len(seq)):
        for index02 in range(1 + index01, len(seq)):
            if (seq[index01] == seq[index02]):
                 return True
    return False



if __name__ == '__main__':

    import printeaSeq
    
    seq = [3, 4, 56, 3.6]
    printeaSeq.printeaSeq('secuencia', seq)
    if(haveDuplicates(seq)):
        print('Yes, duplicates on sequence.\n')
    else:
        print('No, no repeated numbers.\n')

    seq = [3, 4, 56, 4.0]
    printeaSeq.printeaSeq('secuencia', seq)
    if(haveDuplicates(seq)):
        print('Yes, duplicates on sequence.\n')
    else:
        print('No, no repeated numbers.\n')

    seq = []
    printeaSeq.printeaSeq('secuencia', seq)
    if(haveDuplicates(seq)):
        print('Yes, duplicates on sequence.\n')
    else:
        print('No, no repeated numbers.\n')

    seq = [56]
    printeaSeq.printeaSeq('secuencia', seq)
    if(haveDuplicates(seq)):
        print('Yes, duplicates on sequence.\n')
    else:
        print('No, no repeated numbers.\n')