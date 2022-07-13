n = "oomar"
x = reversed("abcdefghijklmnopqrstuvwxyz")
for i in x:
    if i not in n:print(i,end="")
a = list(set(list(n)))
a.sort(key=lambda p:(n.count(p),-ord(p)))
print("".join(a))
