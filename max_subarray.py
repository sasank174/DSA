n = [-1,2,3,4,-2,6,-8,3]
if max(n) < 0:print(-1)
s = 0
for i in range(len(n)):
    for j in range(i,len(n)):
        if sum(n[i:j+1]) > s:s = sum(n[i:j+1])
print(s)