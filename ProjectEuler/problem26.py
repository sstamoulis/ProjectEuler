max_length = 0

for d in range(1000, 1, -1):
    if d < max_length: break
    remainders = []
    r = 1 % d
    while r != 0 and r not in remainders:
        remainders.append(r)
        r = (r * 10) % d

    if r != 0:
        length = len(remainders[remainders.index(r):])
        if length > max_length:
            max_length = length
            print(max_length, d)