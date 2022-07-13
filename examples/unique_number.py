a,b,c = 10,15,0
for i in range(a,b+1):
    s = list(str(i))
    if len(s) == len(set(s)):c+=1
print(c)
