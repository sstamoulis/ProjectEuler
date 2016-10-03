from tools import generate_primes
import itertools as it

n=10001
print(next(it.islice(generate_primes(), n-1, None)))