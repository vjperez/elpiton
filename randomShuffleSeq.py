# implement shuffle (seq), using randint(a,b) from random
# the reusable code is really implementing a random swap on the seq using randint
# the shuffle is implemented on the main, calling swap multiple times
# randint(a, b) returns a randomly distributed integer between a and b, including both

import random
import printeaSeq

def randomSwapOnSeq(seq):
    a = random.randint(0, -1 + len(seq))
    b = random.randint(0, -1 + len(seq))
    if not (a == b):
        seq[a], seq[b] = seq[b], seq[a]


if __name__ == '__main__':
    
    cuantosSwaps = 4
    secuencia = ['uno', 'dos', 'tres', 'cuatro']
    printeaSeq.printeaSeq('secuencia original', secuencia)
    print()

    for i in range( cuantosSwaps ):
        randomSwapOnSeq(secuencia)
        printeaSeq.printeaSeq('secuencia after a swap', secuencia)