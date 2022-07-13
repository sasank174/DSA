from itertools import permutations,combinations,combinations_with_replacement

n = "abc"
x = list(permutations(n))
x = ["".join(i) for i in x]

print("permutations:")
print(*x, sep=" ")
print()
# =================================================================
x = list(combinations(n,1))
x = ["".join(i) for i in x]
print("combinations:")
print(*x, sep=" ")
x = list(combinations(n,2))
x = ["".join(i) for i in x]
print(*x, sep=" ")
x = list(combinations(n,3))
x = ["".join(i) for i in x]
print(*x, sep=" ")
# =================================================================

x = list(combinations_with_replacement(n,1))
x = ["".join(i) for i in x]
print("combinations_with_replacement:")
print(*x, sep=" ")
x = list(combinations_with_replacement(n,2))
x = ["".join(i) for i in x]
print(*x, sep=" ")
x = list(combinations_with_replacement(n,3))
x = ["".join(i) for i in x]
print(*x, sep=" ")
# =================================================================
