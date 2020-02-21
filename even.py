a = []
n = int(input())
for i in range(n):
	x=int(input())
	a.append(x)
print(a)

def eve(a,n):
	s=0
	for i in range(n):
		if a[i]%2==0:
			s=s+a[i]
	print(s)

eve(a,n)