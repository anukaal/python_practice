a = list(map(int,input().split()))
key = int(input())
for i in range(len(a)):
	if key==a[i]:
		print(i)

