from tools import generate_abundant_numbers
import itertools

limit = 20161 #Every integer greater than 20161 can be written as the sum of two abundant numbers.
smallest_abudant = next(generate_abundant_numbers())
abundants = [a for a in itertools.takewhile(lambda x: x<limit-smallest_abudant+1, generate_abundant_numbers())]

canBeWrittenAsAbundant = {}
for i in range(len(abundants)):
    if abundants[i]+ smallest_abudant>limit:break
    for j in range(i,len(abundants)):
        if abundants[i]+abundants[j]<=limit:
            canBeWrittenAsAbundant[abundants[i]+abundants[j]]=True
        else:
            break

i=0
s=0
for n in range(1,limit+1):
    if not canBeWrittenAsAbundant[n]:
        s+=n
    else:
        i+=1
        a=canBeWrittenAsAbundant[i]

print(s)
