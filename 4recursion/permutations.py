def permutations(n,i=0):
    if i == len(n):
        print("".join(n),end=" ")
        return
    
    for j in range(i,len(n)):
        n[i],n[j] = n[j],n[i]
        permutations(n,i+1)
        n[i],n[j] = n[j],n[i]

n = "abc"
permutations(list(n))