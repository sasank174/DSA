def count(n,output=""):
    if n == 1:
        print(output+"1")
        return 1
    if n == 0:
        print(output)
        return 1
    return count(n-2,output+"2") + count(n-1,output+"1")

n = 4
print(count(4))