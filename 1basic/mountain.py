n = [5,6,1,2,3,4,5,4,3,2,0,1,2,3,-2,4]

out = 0
for i in range(1,len(n)-1):
    a,count = min([i,len(n)-i-1]),0
    for j in range(1,a+1):
        if n[i+j] < n[i+j-1] and n[i-j] < n[i-j+1]:count+=1
        else:
            if count > out:out = count
            break
print(out*2+1)