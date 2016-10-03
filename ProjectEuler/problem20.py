from math import factorial
from tools import digit_sum

n=100
f = factorial(n)
s = digit_sum(f)
print(n,f,s)