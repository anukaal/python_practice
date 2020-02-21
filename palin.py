def pal(s):
	d=s[::-1]
	if d==s:
		print('palindrome')
	else:
		print('Not palindrome')

s=input()
pal(s)