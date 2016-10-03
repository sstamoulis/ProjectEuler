from tools import generate_primes

s = 0
limit=2000000
for p in generate_primes():
    if p>=limit: break
    s+=p

print(s)