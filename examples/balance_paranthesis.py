n = "{()}[]"
if n[0] == ")" or n[0] == "]" or n[0] == "}":
    print("NO")
    exit()
t = []
for i in n:
    if i == "(" or i == "[" or i == "{":t.append(i)
    elif (i == ")" and t[-1] == "(") or (i == "]" and t[-1] == "[") or (i == "}" and t[-1] == "{"):t.pop()
    else:
        print("NO")
        exit()
if len(t) == 0:
    print("YES")
