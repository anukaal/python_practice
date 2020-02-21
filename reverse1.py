s = input()
s = list(s)
print(s)
l = len(s)
b = ''
s[0],s[-1]=s[-1],s[0]
b = b.join(s)
print(b)