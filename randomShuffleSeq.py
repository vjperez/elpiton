# implement shuffle (seq), using randint(a,b) from random
# the reusable code is really implementing a random swap on the seq using randint
# the shuffle is implemented on the main, calling swap multiple times
# randint(a, b) returns a randomly distributed integer between a and b, including both

import random

def randomSwapOnSeq(seq):
    a = random.randint(0, -1 + len(seq))
    b = random.randint(0, -1 + len(seq))
    if not (a == b):
        seq[a], seq[b] = seq[b], seq[a]



def randomShuffle(seq, cuantosSwaps):
    for i in range( cuantosSwaps ):
        randomSwapOnSeq( seq )



if __name__ == '__main__':
    import printeaSeq
    
    secuencia = ['uno', 'dos', 'tres', 'cuatro']
    printeaSeq.printeaSeq('secuencia original', secuencia)
    print()

    cuantosSwaps = 1
    randomShuffle(secuencia, cuantosSwaps)
    printeaSeq.printeaSeq('secuencia after 1 swap', secuencia)
    print()
    
    cuantosSwaps = 100
    randomShuffle(secuencia, cuantosSwaps)
    printeaSeq.printeaSeq('secuencia after 101 swaps', secuencia)