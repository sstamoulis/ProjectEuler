from __future__ import division
import math
import operator
import itertools
import copy
import collections

class Cache: #Empty class to act as a C struct
    pass

def generate_primes():
    """ Generate an infinite sequence of prime numbers if no limit is specified.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = generate_primes.dictionary
    
    # Running integer
    q = 1

    c = Cache.primes

    while True:
        q +=1
        if q <= c[-1]:
            for q in itertools.dropwhile(lambda x: x < q, c):
                yield q
        elif q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            Cache.primes.append(q)
            D[q * q] = [q]            
            yield q
        else:
            # q is composite.  D[q] is the list of primes that
            # divide it.  Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

generate_primes.dictionary = {4: [2]}
Cache.primes = [2]

def find_prime_factors(number):
    n = number
    r = {}
    for p in generate_primes():
        if p * p > n: break
        while n % p == 0:
            r[p] = r.setdefault(p,0) + 1
            n = n // p
    if n > 1:
        r[n] = r.setdefault(n,0) + 1
    return r

def is_prime(number):
    """Check if number is prime
    """
    n = number
    if n in Cache.primes: return True
    else:
        if n <= 1: return False
        elif n <= 3: return True
        elif n % 2 == 0 or n % 3 == 0: return False
        i = 5
        while i ** 2 <= n:
            if n % i == 0 or n % (i + 2) == 0: return False
            i+=6
        return True

def binomial(n, k):
    #https://en.wikipedia.org/wiki/Binomial_coefficient#Multiplicative_formula
    denominator = range(1,k + 1)
    numerator = [n + 1 - i for i in denominator]
    b = prod(numerator) / prod(denominator)
    print((b,p))
    return b

def digit_sum(number, base=10): #https://en.wikipedia.org/wiki/Digit_sum
    """
    Get the sum of number's digits, using the given base.
    """
    x,b = number,base
    return sum([(1 / b ** n) * (x % b ** (n + 1) - x % b ** n) for n in range(0, int(math.log(x,b)) + 1)])

def prod(sequence): return reduce(operator.mul, sequence, 1)

def number_to_words(number):
    """
    Converts number up to 9999 to words
    """
    w = number_to_words.dictionary
    n = number
    limit = 9999
    if(n > limit): raise ValueError('Number {n} is over the limit {l}'.format(n=n,l=limit))
    d = get_all_digits(n)
    d = [0] * (4 - len(d)) + d
    result = []
    if d[0] > 0: result.append(w[d[0]] + ' ' + w[1000])
    if d[1] > 0: result.append(w[d[1]] + ' ' + w[100])
    if d[2] == 1: result.append(w[d[2] * 10 + d[3]])
    elif d[2] > 0: result.append(w[d[2] * 10])
    if d[3] > 0 and d[2] != 1: result.append(w[d[3]])
    return ' '.join(result)
    
number_to_words.dictionary = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
     11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',
     18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',
     80:'eighty',90:'ninety',100:'hundred',1000:'thousand'}    

def get_digit(number, position):
    """
    Get the digit at position in number. Position is 0 based and starts at the right.
    """
    n = number
    p = position
    if p > 0:
        d = 10 ** p
        return (n // d) % d
    else:
        return n % 10

def get_all_digits(number):
    """
    Split number into its digits.
    """
    if number == 0: return 0
    n = number if number > 0 else -number
    digits = []
    while n != 0:
        n, remainder = n // 10, n % 10
        digits.insert(0, remainder)
    return digits

def find_all_factors(number):
    prime_factors = find_prime_factors(number)
    values = [[(factor**e) for e in range(exp+1)] for factor, exp in prime_factors.viewitems()]
    results = [prod(x) for x in itertools.product(*values)]
    return results

def find_proper_factors(number):
    return find_all_factors(number)[:-1]

def generate_amicable_pairs(limit=None):
    s = generate_amicable_pairs.sum_of_proper_factors
    for x in itertools.count(s.keys()[-1] + 1):
        if limit is not None and x > limit: return
        if x in s: factors_sum = s[x]
        else: factors_sum = int(sum(find_proper_factors(x)))
        if factors_sum > x: s[x] = factors_sum
        if factors_sum in s and s[factors_sum] == x:
            yield factors_sum, x

generate_amicable_pairs.sum_of_proper_factors = collections.OrderedDict([(220, 284)])

def generate_abundant_numbers():
    # https://en.wikipedia.org/wiki/Abundant_number#Properties
    a = Cache.abundant_numbers
    p = Cache.perfect_numbers
    d = Cache.deficient_numbers
    n = 1
    while True:
        if n < a[-1]:
            for n in itertools.dropwhile(lambda x: x < n, a):
                yield n
        else:
            s = sum(find_proper_factors(n))
            if s > n:
                a.append(n)
                yield n
            elif s == n:
                p.append(n)
            else:
                d.append(n)
        n+=1
   
Cache.abundant_numbers = [12]
Cache.perfect_numbers = []
Cache.deficient_numbers = []