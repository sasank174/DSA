n = list("prateekbhaiya")
l,i,j = [],0,1

while j<len(n):
    x = n[i:j]
    if len(x) == len(set(x)):
        if len(x)>len(l):l = x
        j += 1
    elif len(x) > len(set(x)):i = x.index(x[-1])+1+i
    elif len(x) < len(l):j += 1
    elif len(x) > len(l):i += 1
print("".join(l))