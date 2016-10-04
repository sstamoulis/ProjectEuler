import itertools as it

limit=100

results = set()
for a,b in it.product(range(2,limit+1),range(2,limit+1)):
    results.add(a**b)

print(len(results))