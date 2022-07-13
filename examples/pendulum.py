n,t = [1,2,3,4,5],[]
n.sort()
for i in range(len(n)):
    if i%2==0:t.append(n[i])
    else:t.insert(0,n[i])
print(t)