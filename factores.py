n = 36

factors = []
for isFactor in range(1, n+1):
    if n % isFactor == 0:
        factors.append( isFactor )

for i in range(len(factors)):
    print(factors[i])
