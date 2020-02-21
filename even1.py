a = []
n = int(input())
for i in range(n):
	x=int(input())
	a.append(x)
print(a)


def sx(a,n):
	s=0
	for i in range(0,n,2):
		s=s+a[i]
	print(s)