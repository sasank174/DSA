n,a,b,l,r = [0,1,0,2,1,0,1,3,2,1,2,1],[],[],0,0
for i in range(len(n)):
    if n[i] > l:l = n[i]
    a.append(l)
    if r < n[len(n)-i-1]:r = n[len(n)-i-1]
    b.append(r)
b.reverse()

out = [min(a[i],b[i]) - n[i] for i in range(len(n))]
print(out)
print(sum(out))