import math

n = [1,2,3,4,5]
t = []
for i in range(len(n)):
    p = n.copy()
    p.pop(i)
    t.append(math.prod(p))
print(t)