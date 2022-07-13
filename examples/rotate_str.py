# rotate str by n positions L or R

s,n,x = input(),int(input()),input()
for i in range(n):
    if x == "L":s = s[1:]+s[0]
    if x == "R":s = s[-1]+s[:-1]
print(s)