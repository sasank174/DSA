n = [1,2,3,4,5,6,7,8,9,15]
s = 18
t = []
for i in range(len(n)//2):
    for j in range(len(n),len(n)//2,-1):
        a = s - (n[i] + n[j-1])
        if a in n:
            x = sorted([n[i],n[j-1],a])
            if x not in t:t.append(x)
print(t)