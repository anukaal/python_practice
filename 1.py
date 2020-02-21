arr=list(map(int,input().split()))

n=len(arr)
print(arr)
p=int(input())
ele=int(input("Enter a number to be inserted"))
arr.append(0)
for i in range(n,p-1,-1):
	arr[i]=arr[i-1]
	print(arr)
	print(i)
arr[i]=ele

print(arr)
	
