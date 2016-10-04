from tools import is_prime
# |a|< 1000 --> -1000 < a < 1000
# |b|<=1000 --> -1000 <=b <=1000

def quadratic_formula(a, b):
    return lambda n: n**2 + a*n + b

def superscript(n):
    if n==1: return unichr(0x00b9)
    elif n==2 or n==3: return unichr(0x00b0+n)
    else: return unichr(0x2070+n)

def print_formula(a,b):
    if a>0:
        print(u'n{} + {a:>3}n + {b}'.format(superscript(2),a=a,b=b))
    else:
        print(u'n{} - {a}n + {b}'.format(superscript(2),a=-a,b=b))

max_primes = 0
coefficients = None,None
for a in range(-999,1000):
    for b in range(2, 1001):
        q = quadratic_formula(a,b)
        n=0
        count=0
        while is_prime(q(n)):
            count+=1
            n+=1
        if count > max_primes:
            max_primes=count
            coefficients = a,b
            print_formula(a,b)

print('Maximum number of primes is {count}. Given by formula:'.format(count=max_primes))
print_formula(a,b)
