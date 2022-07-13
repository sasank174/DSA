n = "sumit ambuj himanshu ambuj ambuj"
n = n.split()
s = list(set(n))
s.sort(key=lambda x:x.lower())
for i in s:
    print(i,n.count(i))