from os import path

with open(path.relpath(path.join('data','problem22','data.txt')), 'r') as f:
    names = sorted([x[1:-1] for x in f.read().split(',')])

result = sum(i * sum(abs(64 - ord(c)) for c in n) for i,n in enumerate(names, start=1))
print(result)