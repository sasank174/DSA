n = [1,2,3,1,4,5,2,3,6]
k = 3
l = []
for i in range(len(n)-k+1):
    l.append(max(n[i:i+k]))
print(l)