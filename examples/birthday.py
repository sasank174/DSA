n = [1,6]
k = 3

for i in range(k-2):
    n.append((n[-1]+2)*2 - n[-2])
print(n[-1])