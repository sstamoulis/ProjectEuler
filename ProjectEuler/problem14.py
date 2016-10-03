result = 0, 0
for n in range(1000000-1,1,-1):
    x=n
    c=1
    while x>1:
        if x%2==0: x = x/2
        else: x= 3*x+1
        c+=1
    if c>result[0]: 
        result=c, n
        print(result)
