#use factores02 y printeaSeq to compute gcf

#should printes checlk for instance of str and instance of seq ?!?!

import factores02

def gcf(a, b):
    if isinstance(a, int) and isinstance(b, int) and a > 1 and b > 1:
        factoresA = factores02.getFactors(a)
        factoresB = factores02.getFactors(b)

        indexA = -1 + len(factoresA)
        indexB = -1 + len(factoresB)
        while indexA > 0 and indexB > 0:
            if factoresA[indexA] > factoresB[indexB]:
                while factoresA[indexA] > factoresB[indexB]:
                    indexA -= 1
                    if factoresA[indexA] == factoresB[indexB]:
                        return factoresA[indexA]  #could return either factor, they are equal... and this number is the gcd

            elif factoresB[indexB] > factoresA[indexA]:
                while factoresB[indexB] > factoresA[indexA]:
                    indexB -= 1
                    if factoresB[indexB] == factoresA[indexA]:
                        return factoresB[indexB]  #could return either factor, they are equal... and this number is the gcd
            else:
                return factoresA[indexA]  #could return either factor, they are equal... and this number is the gcd

        #if we get down here... after the while ... one of the indexes is zero (factor is = to 1) ... gcd is 1
        return 1    
    else:
        raise Exception('Necesito anteros mayores que 1 !')


if __name__ == '__main__':
    import printeaSeq

    s = 12
    factoresS = factores02.getFactors(s)
    t = 48
    factoresT = factores02.getFactors(t)

    print('primer numero:', s, sep=' ', end='\n')
    printeaSeq.printeaSeq('factores', factoresS )
    print('segundo numero:', t, sep=' ', end='\n')
    printeaSeq.printeaSeq('factores', factoresT )
    
    print('gcf:', gcf(s, t), sep=' ', end='\n--------------\n\n')



    s = 36
    factoresS = factores02.getFactors(s)
    t = 12
    factoresT = factores02.getFactors(t)

    print('primer numero:', s, sep=' ', end='\n')
    printeaSeq.printeaSeq('factores', factoresS )
    print('segundo numero:', t, sep=' ', end='\n')
    printeaSeq.printeaSeq('factores', factoresT )
    
    print('gcf:', gcf(s, t), sep=' ', end='\n---------------\n\n')



    s = 36
    factoresS = factores02.getFactors(s)
    t = 32
    factoresT = factores02.getFactors(t)

    print('primer numero:', s, sep=' ', end='\n')
    printeaSeq.printeaSeq('factores', factoresS )
    print('segundo numero:', t, sep=' ', end='\n')
    printeaSeq.printeaSeq('factores', factoresT )
    
    print('gcf:', gcf(s, t), sep=' ', end='\n---------------\n\n')



    s = 10
    factoresS = factores02.getFactors(s)
    t = 32
    factoresT = factores02.getFactors(t)

    print('primer numero:', s, sep=' ', end='\n')
    printeaSeq.printeaSeq('factores', factoresS )
    print('segundo numero:', t, sep=' ', end='\n')
    printeaSeq.printeaSeq('factores', factoresT )
    
    print('gcf:', gcf(s, t), sep=' ', end='\n---------------\n\n')


    s = 15
    factoresS = factores02.getFactors(s)
    t = 32
    factoresT = factores02.getFactors(t)

    print('primer numero:', s, sep=' ', end='\n')
    printeaSeq.printeaSeq('factores', factoresS )
    print('segundo numero:', t, sep=' ', end='\n')
    printeaSeq.printeaSeq('factores', factoresT )
    
    print('gcf:', gcf(s, t), sep=' ', end='\n---------------\n\n')



    s = 2
    factoresS = factores02.getFactors(s)
    t = 2
    factoresT = factores02.getFactors(t)

    print('primer numero:', s, sep=' ', end='\n')
    printeaSeq.printeaSeq('factores', factoresS )
    print('segundo numero:', t, sep=' ', end='\n')
    printeaSeq.printeaSeq('factores', factoresT )
    
    print('gcf:', gcf(s, t), sep=' ', end='\n---------------\n\n')
