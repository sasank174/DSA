n = [10,2,-2,-20,10]
k = -10

i,j,c = 0,1,0

while i<=j and j<=len(n):
    x = n[i:j]
    if sum(x)==k:c += 1
    if j == len(n):i+=1
    else:j+=1

print(c)