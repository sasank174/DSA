n = [0,1,1,1,1,2,2,2,3,4,4,5,10]
s = 2
i,j = 0,len(n)-1

while i<=j:
    mid = (i+j)//2
    if n[mid]<s:i = mid+1
    elif n[mid]>s:j = mid-1
    else:a,j = mid,mid-1
i,j = a,len(n)-1
while i<=j:
    mid = (i+j)//2
    if n[mid]<s:i = mid+1
    elif n[mid]>s:j = mid-1
    else:b,i = mid,mid+1
print(b-a+1)