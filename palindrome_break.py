p = "abccba"
# p = "aaaa"
if len(p) == 1:print("")
elif len(set(p)) == 1 and p[0] != "a":print("a"+p[1:])
elif len(set(p)) == 1 and p[0] == "a":print(p[:-1]+"b")
else:
    for i in range(len(p)):
        if p[i] != "a":
            print(p[:i]+"a"+p[i+1:])
            break