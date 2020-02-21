a = []
n = int(input())
for i in range(n):
	x=int(input())
	a.append(x)
print(a)

def asd(a,n):
	m = 0
	for i in range(n):
		if a[i]>m:
			m = a[i]
	print(m)
asd(a,n)