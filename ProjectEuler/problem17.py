from tools import number_to_words

s = 0
for i in range(1,1000+1):
    w = number_to_words(i)
    l = len(w.replace(' ',''))
    s+=l
    print(s,i,w,l)