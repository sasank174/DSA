from itertools import permutations

n = [0,1,2,3]
n = list(permutations(n))
n = [i for i in n if i[0] != 0 and i[1] != 1 and i[2] != 2 and i[3] != 3]
print(n)
print(len(n)%100000007)