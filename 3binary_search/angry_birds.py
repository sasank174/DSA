def check(n,d,b):
    s = n[0]
    c = 1
    for i in range(1,len(n)):
        # print(s,n[i],c)
        if n[i] - s >= d:
            c += 1
            s = n[i]
        if c == b:
            return True
    return False

n = [1,2,4,8,9]
b = 3
i,j = 1,n[-1]-n[0]
while i<=j:
    mid = (i+j)//2
    if check(n,mid,b):a,i = mid,mid+1
    else:j = mid-1
print(a)
