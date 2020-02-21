a = input()
for i in a:
	if i==',':
		print(a.replace(',','.'))
		break
	elif i=='.':
		print(a.replace('.',','))
		break