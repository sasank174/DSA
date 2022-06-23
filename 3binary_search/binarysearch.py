n = [1,2,10,11,19,29,28]
s = 1
i,j = 0,len(n)-1
while i<=j:
    if n[(i+j)//2]<s:i = (i+j)//2+1
    elif n[(i+j)//2]>s:j = (i+j)//2-1
    else:
        print((i+j)//2)
        break