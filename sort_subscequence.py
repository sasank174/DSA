from itertools import combinations

s = "abcd"


l = []
for i in range(1, len(s)+1):
    t = list(combinations(s, i))
    t.sort(key=lambda x:x)
    l.extend(t)

l = [''.join(x) for x in l]

print(l)