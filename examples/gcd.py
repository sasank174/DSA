a,b = 11,20
while(a!=0):
    c = a
    a = b%a
    b = c
print(b)