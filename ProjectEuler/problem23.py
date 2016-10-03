from tools import generate_abudant_numbers
import itertools

limit = 28123
abudant_numbers = [x for x in itertools.takewhile(lambda x: x<20161, generate_abudant_numbers())]
smallest_abudant = abudant_numbers[0]
s = 0
for n in range(smallest_abudant + 1, 28123 + 1):
    for a in abudant_numbers:
        if a > n - smallest_abudant: break
        if n - a in abudant_numbers:
            s+=n
            break