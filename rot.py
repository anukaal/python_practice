a = []
n = int(input())
for i in range(n):
	x=int(input())
	a.append(x)
print(a)

def rot(a,n):
	for i in range(n):
		temp = a[n-1]
		for j in range(n-1,0,-1):
			a[j]=a[j-1]
			print(a)
		a[0] = temp
		print(a)

rot(a,n)