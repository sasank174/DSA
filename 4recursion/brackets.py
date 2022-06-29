def countways(o,n,open,close,i):
    if i == 2*n:
        print(o)
        return 
    if open < n:
        countways(o+"(",n,open+1,close,i+1)
    if close < open:
        countways(o+")",n,open,close+1,i+1)

n = 5
o = ""
countways(o,n,0,0,0)