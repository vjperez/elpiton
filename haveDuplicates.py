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
    seq = [3, 4, 56, 3.6]
    if(haveDuplicates(seq)):
        print('Yes, duplicates on sequence.')
    else:
        print('No, no repeated numbers.')

    seq = [3, 4, 56, 4.0]
    if(haveDuplicates(seq)):
        print('Yes, duplicates on sequence.')
    else:
        print('No, no repeated numbers.')

    seq = []
    if(haveDuplicates(seq)):
        print('Yes, duplicates on sequence.')
    else:
        print('No, no repeated numbers.')

    seq = [56]
    if(haveDuplicates(seq)):
        print('Yes, duplicates on sequence.')
    else:
        print('No, no repeated numbers.')