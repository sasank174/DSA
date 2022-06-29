def countways(arr,n,i,x):
    if i == n:
        if x == 0:return 1
        else:return 0
    
    inc = countways(arr,n,i+1,x-arr[i])
    exc = countways(arr,n,i+1,x)
    return inc + exc

arr = [1,2,3,4,5]
x = 6

print(countways(arr,len(arr),0,x))