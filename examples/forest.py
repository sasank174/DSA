n = ["TTTWW","TWWTT","TWWTT","TWTTT","WWTTT"]
count = 0
max = 0

def check(i,j):
    global count,n
    if i<0 or j<0 or i>=len(n) or j>=len(n):
        return
    
    if n[i][j] == "T":
        x = list(n[i])
        x[j] = "W"
        n[i] = "".join(x)
        count += 1
        check(i+1,j)
        check(i-1,j)
        check(i,j+1)
        check(i,j-1)

for i in range(len(n)):
    for j in range(len(n)):
        if n[i][j] == "T":
            check(i,j)
            if count > max:max = count
            count = 0
print(max)
