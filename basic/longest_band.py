n = [1,9,3,0,18,5,2,4,10,7,12,6]

n.sort()
o = 0
for i in range(len(n)-1):
    count = 0
    for j in range(1,len(n)-i):
        if n[i+j]-n[i+j-1] == 1:count+=1
        else:
            if count > o:o = count
            break
print(o+1)