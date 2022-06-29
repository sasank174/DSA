from sqlalchemy import null


keypad = ["","","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]

def countways(n,o,i=0):
    if i == len(n):
        print(o)
        return
    current_digit = n[i]
    if current_digit == "0" or current_digit == "1":countways(n,o,i+1)
    for k in range(len(keypad[int(current_digit)])):
        countways(n,o+keypad[int(current_digit)][k],i+1)
    return

n = "234"
o = ""
countways(n,o)