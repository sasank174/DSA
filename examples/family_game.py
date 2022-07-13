def check(t,n):
    for i in range(len(s)):
        if s[i] == "y":print(n.pop(i%len(n)))

n,s = 3,list("xyx")
n = [str(i) for i in range(1,n+1)]

while(len(n)>1):
    # print(n)
    check(s,n)
print(n)