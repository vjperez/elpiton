import printeaSeq

#v must be an integer and must be > than 1
def getFactors(v):
    if isinstance(v, int) and v > 1:
        #using comprehension syntax: list comprehension
        factors = [isFactor for isFactor in range(1, v+1) if v % isFactor == 0]
        return factors
    else: 
        raise Exception('argumento no es int mayor que 1.')



if __name__ == '__main__':
    x = 36
    print('2 ways to print factors of ', x)

    f = getFactors(x)
    for i in range(len( f )):
        print( f[i] )

    print('\n\n')

    for factor in f:
        print(factor, '          ', sep='', end='')

    print('\n\ntercera forma .... importing la funcion printeaSeq')
    printeaSeq.printeaSeq('factores :', f)

