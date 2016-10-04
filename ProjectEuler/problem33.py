from tools import get_all_digits, prod
from fractions import gcd, Fraction

nominators = []
denominators = []
fractions = []
for n in range(10,100):
    for d in range(n+1,100):
        n_digits = get_all_digits(n)
        d_digits = get_all_digits(d)
        if 0 in d_digits: continue
        common_digits = set(n_digits).intersection(d_digits)
        if len(common_digits)!=1: continue
        c = common_digits.pop()
        f1 = Fraction(n,d)
        n_digits.remove(c)
        d_digits.remove(c)
        f2 = Fraction(n_digits[0],d_digits[0])
        if f1==f2:
            nominators.append(n)
            denominators.append(d)
            fractions.append(f1)
        

print(nominators)
print(denominators)
print(fractions)
nom_prod = prod(f.numerator for f in fractions)
den_prod = prod(f.denominator for f in fractions)
print(den_prod // gcd(nom_prod,den_prod))