a = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
b = [1]
for i in range(2,27):b.append(i*b[i-2]+b[i-2])
n = int(input())
print(b)
s = ""
for i in b[::-1]:
    if n%i == 0:
        n = n//i
        s = s + "A"*n
        break
    elif n%i<n:
        p = n//i
        n = n - p*i
        s = s + (a[b.index(i)])*p
print("".join(sorted(s)))