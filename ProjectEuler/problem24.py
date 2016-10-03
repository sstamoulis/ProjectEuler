import itertools

p = next(itertools.islice(itertools.permutations(range(10)), 1000000-1, None))
print(''.join(str(x) for x in p))