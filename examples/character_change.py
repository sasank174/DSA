import re
vowels = ['a', 'e', 'i', 'o', 'u']
consonents = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
s1 = "I am a string"
s2 = "I am a string"
s3 = "I am a string"
print(s3.lower())
s1 = re.sub('[aeiou]', '$', s1)
s2 = re.sub('[^aeiou]', '$', s2)
print(s1)
print(s2)