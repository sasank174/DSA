# no of minutes to get a palindrome time

def palindrome(t):
    if t[0] == t[1][::-1]:return True
    else:return False

n = "05:39"
t = list(map(str, n.split(":")))
i = 0
while(not palindrome(t)):
    a,b= int(t[0]),int(t[1])+1
    if b == 60:
        a+=1
        t[0],t[1] = str(a),"00"
        if len(str(t[0])) == 1:t[0] = "0"+t[0]
    else:
        t[1] = str(b)
        if len(str(t[1])) == 1:t[1] = "0"+t[1]
    if t[0] == "24":t[0] = "00"
    i+=1


print(i)