a = []
n = int(input())
for i in range(n):
	x=int(input())
	a.append(x)
print(a)

def inn(a,n):
	x=int(input())
	ele = int(input("Enter number to be imserted"))
	a.append(0)
	for i in range(n , x , -1):
		a[i]=a[i-1]	
		a[i-1]=ele
	print(a)


inn(a,n)