# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import itertools as it

n=20
dividers = []
for i in range(20,1,-1):
    add=True
    for d in dividers:
        if d%i==0:
            add= False
            break
    if add: dividers.append(i)

dividers.remove(20)    
for n in it.count(20,20):
    result=True
    for d in dividers:
        if n%d!=0:
            result=False
            break
    if result: break

print(n)