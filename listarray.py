def update(arr,n):
	for i in range(n):
		arr[i]=arr[i]+2
	print(arr)

n=int(input())
arr=[]
for i in range(n):
	x=int(input())
	arr.append(x)
print(arr)
update(arr,n)
print(arr)