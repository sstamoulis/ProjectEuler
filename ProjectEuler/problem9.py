# https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple

p=1000
found= False
for a in range(1,p/3):
    for b in range(a,p/2):
        c=p-a-b
        if(a*a+b*b==c*c):
            found=True
            break
    if found: break

print(a*b*c)