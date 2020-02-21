s = input()
l = len(s)
if (s[l-1]=='g' and s[l-2]=='n' and s[l-3]=='i'):
	s = s+'ly'
else:
	s = s+'ing'

print(s)