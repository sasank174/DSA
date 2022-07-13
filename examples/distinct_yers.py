import re
n = "UN was established on 24-10-1945. India got freedom on 15-08-1947"
x = re.findall(r'[0-9]{2}-[0-9]{2}-[0-9]{4}', n)
print(x)