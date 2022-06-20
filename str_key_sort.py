index = 2
reversed = False
output="numeric"

n = [["92","022"],["82","12"],["77","13"]]

if output == "numeric":
    n.sort(key=lambda x:int(x[index-1]),reverse=reversed)
elif output == "lexicographic":
    n.sort(key=lambda x:x[index-1],reverse=reversed)
print(n)