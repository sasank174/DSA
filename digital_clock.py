n = 1180
n = 125

a= [str(n//60).zfill(2), str(n%60).zfill(2)]
a = ':'.join(a)
print(a)