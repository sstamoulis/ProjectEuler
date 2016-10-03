from tools import generate_fibonacci

limit = 10**999

for i,f in enumerate(generate_fibonacci()):
    if f > limit: break

print(i)