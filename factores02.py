n = 36

#using comprehension syntax: list comprehension
factors = [isFactor for isFactor in range(1, n+1) if n % isFactor == 0]

for i in range(len(factors)):
    print(factors[i])
