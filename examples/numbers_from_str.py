s = "hello this is alpha 5051 and 9475"
s = s.split()
s = [int(i) for i in s if i.isdigit() and "9" not in i]

if len(s) > 0:print(max(s))
else:print(-1)