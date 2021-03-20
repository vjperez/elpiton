#is there a pair whose product is odd
#from a seq of integers

# 2 * 5.5 !?

seq = [3, 4, 7, 6, 9, 0.5, ]

for i1 in range(-1 + len(seq)):
    for i2 in range(1 + i1, len(seq)):
        if   float(seq[i1] * seq[i2]) % 2 == 1.0: 
            print(seq[i1], seq[i2], 'producto impar =', seq[i1] * seq[i2])
        elif float(seq[i1] * seq[i2]) % 2 == 0.0:
            print(seq[i1], seq[i2], 'producto par =',   seq[i1] * seq[i2])
        else: 
            print(seq[i1], seq[i2], 'producto float ni par, ni impar =',   seq[i1] * seq[i2])