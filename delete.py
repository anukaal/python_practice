a = []
n = int(input())
for i in range(n):
	x=int(input())
	a.append(x)
print(a)

def dl(a,n):
	x = int(input('Enter pos of number to be deleted'))
	for i in range(x,n-1):
		a[i]=a[i+1]
	del a[n-1]
	print(a)

dl(a,n)