# prime factors should be 2, 3 and 5

def prime(i):
    t = [j for j in range(2, i+1) if i%j == 0]
    t = [(p%2==0 or p%3==0 or p%5==0) for p in t]
    return all(t)

x,n,i=[1,2,3],int(input()),4
while(len(x)<n):
    if prime(i):x.append(i)
    i+=1
print(x)