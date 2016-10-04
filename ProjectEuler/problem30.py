from tools import get_all_digits

results =[]
for x in range(2,6*9**5):
    if sum(d**5 for d in get_all_digits(x)) == x:
        results.append(x)
        print(x)

print(results)
print(sum(results))