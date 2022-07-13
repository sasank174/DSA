n,p = 3,5

def factorial(n):
    t = 1
    for i in range(2,n+1):t *= i
    return t
n = factorial(n)
s = 0
while(p**s<=n):
    if n%(p**s) == 0:t = s
    s+=1
print(t)