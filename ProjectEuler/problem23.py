from tools import generate_abundant_numbers, Timer
import itertools
import sys

limit = 20161 #Every integer greater than 20161 can be written as the sum of two abundant numbers.
smallest_abudant = next(generate_abundant_numbers())
print('Generating abundants')
with Timer() as t:
    abundants = [a for a in itertools.takewhile(lambda x: x<limit-smallest_abudant+1, generate_abundant_numbers())]
print('Complete in {} seconds'.format(t.interval))

def is_abundant_sum(n):
    for i in abundants:
        if i < n:
            if (n-i) in abundants:
                return True
    return False

s=0
last_percentage=0
for n in range(1, limit+1):
    if not is_abundant_sum(n):
        s+=n
        current_percentage=n*100//limit
        if current_percentage>last_percentage:
            last_percentage=current_percentage
            sys.stdout.write('\r{:>3}%'.format(current_percentage))
            sys.stdout.flush()
            #print(s)
sys.stdout.write('\n')
print(s)
