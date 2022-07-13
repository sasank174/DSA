n = "][(a+b)+c)"
a = []
o = ""
for i in n:
    if i in ["(", "[", "{"]:
        a.append(i)
    elif i in [")", "]", "}"]:
        if len(a) == 0:
            o = "NO"
            break
        else:
            if i == ")" and a[-1] == "(":
                a.pop()
            elif i == "]" and a[-1] == "[":
                a.pop()
            elif i == "}" and a[-1] == "{":
                a.pop()
            else:
                o = "NO"
                break
    else:
        continue
if len(a) == 0 and o == "":
    print("YES")
else:
    print("NO")
