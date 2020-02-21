s = input()
s = s.split()
for i in range(len(s)):
	s[i].capitalize()
for i in range(len(s)):
	if(i==len(s)-1):
		print(s[i])
	else:
		print(s[i][0]+'.')
