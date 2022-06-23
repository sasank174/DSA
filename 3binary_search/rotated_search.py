n = [4,5,6,7,0,1,2,3]
key = 3
i,j = 0,len(n)-1
while i<=j:
    mid = (i+j)//2
    if n[mid] == key:
        print(mid)
        break
    if n[i]<=n[mid]:
        # left
        if key >= n[i] and key <= n[mid]:j = mid-1
        else:i = mid+1
    else:
        # right
        if key >= n[mid] and key <= n[j]:i = mid+1
        else:j = mid-1