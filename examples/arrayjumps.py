a = [3,4,2,1,2,3,7,1,1,1,2,5]
x = []
t = "".join([str(i) for i in a])
def maxjumps(a,i=0,s=""):
    global t
    if len(s) > len(t) or i>=len(a):return 0
    if i == len(a)-1:
        t = s+str(a[i])
        return 
    for j in range(1,a[i]+1):maxjumps(a,i+j,s+str(a[i]))



maxjumps(a)
x = [i for i in x if len(i)==5]
print(t)
print(x)