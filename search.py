a = []
n = int(input())
for i in range(n):
	x=int(input())
	a.append(x)
print(a)

def srh(a,n):
	k=0
	x = int(input('Enter no to be searched'))
	for i in range(n):
		if (a[i]==x):
			k=1
	if (k==1):
		print('Found')
	else:
		print('Not found')

srh(a,n)