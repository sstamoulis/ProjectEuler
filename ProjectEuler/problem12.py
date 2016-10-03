#http://stackoverflow.com/questions/110344/algorithm-to-calculate-the-number-of-divisors-of-a-given-number

import itertools as it
from math import sqrt, ceil
from tools import find_prime_factors

limit = 500

for n in it.count(1):
    t = n*(n+1)/2
    prime_factors = find_prime_factors(t)
    f=1
    for p in prime_factors:
        c = prime_factors[p]
        f*=c+1
    #print((t,prime_factors,f))
    if f>limit: break
print((t,prime_factors,f))