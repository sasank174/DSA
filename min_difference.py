a,b = [23,5,10,17,30],[26,134,135,14,19]
a.sort()
b.sort()
p,q = a[0],b[0]
d = abs(a[0]-b[0])
# [5, 10, 17, 23, 30]
# [14, 19, 26, 134, 135]
for i in range(len(a)):
    for j in range(len(b)):
        if abs(a[i]-b[j]) < d:
            d = abs(a[i]-b[j])
            p,q = a[i],b[j]
print(p,q)