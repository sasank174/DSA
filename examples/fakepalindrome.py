n = "ABAB"
t = []
for i in range(len(n)):
    for j in range(i,len(n)):
        if n[i:j+1] == n[i:j+1][::-1]:
            t.append(n[i:j+1])
print(t)