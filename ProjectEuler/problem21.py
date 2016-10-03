#https://en.wikipedia.org/wiki/Amicable_numbers#Euler.27s_rule

from tools import generate_amicable_pairs

s =0
for a,b in generate_amicable_pairs(10000-1):
    s+=a+b
    print(s,(a,b))
