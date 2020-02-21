s = input("Input: ")
tr = input("String to replace: ")
tw = input("string replace with: ")
if tr in s:
	s = s.replace(tr,tw)
	print(s)
else:
	print('No substring')