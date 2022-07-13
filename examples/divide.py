n = [1,3,9,7]
c = 0

while len(set(n)) > 1:
    print(n)
    x = n.index(min(n))
    i = x+1
    if x+1 == len(n):i = 0
    if n[x-1] > n[i]:n[x],n[x-1] = n[x]+1,n[x-1]-1
    else:n[x],n[i] = n[x]+1,n[i]-1
    c += 1
print(c)