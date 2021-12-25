import printeaSeq


def getFactors(v):
    if isinstance(v, int) and v > 1:
        #using comprehension syntax: list comprehension
        factors = [isFactor for isFactor in range(1, v+1) if v % isFactor == 0]
        return factors
    else: 
        raise Exception('argumento no es int mayor q 1.')



if __name__ == '__main__':
    print('2 ways to print factors of 24')
    x = 24
    f = getFactors(x)
    for i in range(len( f )):
        print( f[i] )

    print('\n\n')

    for factor in f:
        print(factor, '          ', sep='', end='')

    print('\n\ntercera forma .... importing la funcion printeaSeq')
    printeaSeq.printeaSeq('factores de 24:', f)

