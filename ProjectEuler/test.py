import itertools
import tools

for n in itertools.count():
    print(tools.find_all_factors(n))
    print(tools.find_proper_factors(n))
    print()