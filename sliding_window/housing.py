n = [1,3,2,1,4,1,3,2,1,1,2]
i,j = 0,0
s = 8

while j<len(n):
    x = n[i:j]
    if sum(x) == s:
        print(x)
        j += 1
    elif sum(x) > s:i += 1
    elif sum(x) < s:j += 1