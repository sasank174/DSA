s,c = list("hello"),list("elo")
i,j,t = 0,len(c),""

while i<j  and j<=len(s):
    x,n = s[i:j],1
    for p in set(c):
        if c.count(p) > x.count(p):
            n = 0
            break
    if n:
        t = x
        i+=1
    else:j += 1
print(t)