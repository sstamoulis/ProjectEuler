import collections
import itertools as it
from tools import get_all_digits

def any_duplicates(list):
    seen=set()
    for item in list:
        if item in seen: return True
        seen.add(item)
    return False

products=set()
pandigital = collections.Counter([1,2,3,4,5,6,7,8,9])

for a in range(2, 9876):
    for b in it.count(a):
        c=a*b
        all_digits = get_all_digits(a)+get_all_digits(b)+get_all_digits(c)
        if len(all_digits)>9:
            break
        if collections.Counter(all_digits) == pandigital:
            print('{} x {} = {}'.format( a,b,c))
            products.add(c)

print(sum(products))