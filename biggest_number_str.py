from itertools import permutations

n = [10,11,20,30,3]
n = list(map(str, n))
l = list(permutations(n))
l = [int(''.join(i)) for i in l]
print(max(l))
