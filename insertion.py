s = input("sting: ")
x = input("Character to insert: ")
n = int(input("Postion: "))
k = len(s)
b = s[0:n-1]+x+s[n:k]
print(b)