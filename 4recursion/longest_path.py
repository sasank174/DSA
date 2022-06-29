t = []
def path(p,o="",i=0,j=0):
    if i>=len(p) or j>=len(p) or i<0 or j<0:
        return
    if i == len(p)-1 and j == len(p)-1:
        o+=str(p[i][j])
        t.append(o)
        return
    if p[i][j] == 1:
        print(o,i,j,p)
        p[i][j] = "X"
        path(p,o+"1",i+1,j)
        path(p,o+"1",i-1,j)
        path(p,o+"1",i,j+1)
        path(p,o+"1",i,j-1)
        

n = [[1,1,1,1],[1,1,1,1],[0,0,1,1],[1,1,1,1]]
path(n)
print(t)
t = [len(i)-1 for i in t]
print(t)
#  1 1 1 1
#  1 1 1 1
#  0 0 1 1
#  1 1 1 1