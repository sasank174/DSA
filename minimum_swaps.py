n = [5,4,3,2,1]
# n = [10,11,5,4,3,2,1]
t = sorted(n)
swaps = 0
for i in range(len(n)):
    if n[i] != t[i]:
        swaps += 1
        p = n.index(t[i])
        n[i], n[p] = n[p], n[i]
print(swaps)