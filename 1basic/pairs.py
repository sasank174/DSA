n = [10,5,2,3,-6,9,11]
s = 4
def pairs(n,s):
    t = []
    for i in n:
        x = s - i
        if x in n and x!=i and sorted([i,x]) not in t:t.append(sorted([i,x]))
    return t
print(pairs(n,s))