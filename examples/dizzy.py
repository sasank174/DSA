# 3
# 1 2 3
# 4 5 6 
# 8 9 10
# output: 1 2 3 6 9 8 7 4 5


from math import ceil


n = [[1,2,3],[4,5,6],[7,8,9]]
# n = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
count = 1
round = ceil(len(n)/2)
print(round)
for i in range(round):
    for j in range(i,len(n)-i):print(n[i][j],end=' ') # print the first row
    for j in range(i+1,len(n)-i):print(n[j][len(n)-i-1],end=' ') # print the last column
    for j in range(len(n)-i-2,i,-1):print(n[len(n)-i-1][j],end=' ') # print the last row
    for j in range(len(n)-i-1,i,-1):print(n[j][i],end=' ') # print the first column