s = "aaaabcccccaaa"
c = 1
t = ""
for i in range(1,len(s)):
    if s[i] == s[i-1]:c += 1
    else:
        t,c = t + s[i-1] + str(c),1
t = t + s[i-1] + str(c)
if len(s) > len(t):print(t)
else:print(s)