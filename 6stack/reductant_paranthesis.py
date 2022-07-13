# n = "((a+b)+c)"
n = "(a+b+c)"
i,stack,operator,output = 0,[],False,""
while i < len(n):
    if n[i] in ")":
        while stack[-1] != "(" and len(stack)>0:
            x = stack.pop()
            if x in "+-*/":operator = True
        if operator:
            stack.pop()
            operator = False
            i+=1
        else:
            output = "NO"
            break
    else:
        stack.append(n[i])
        i+=1

print(stack)
if output == "":output = "YES"
print(output)