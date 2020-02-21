n,m=input().split()
n=int(n)
m=int(m)
arr=list(map(int,input().split()))[:m]
arr.sort()
print(arr)
count=[]
for i in arr:
	flag=0
	for j in arr:
		if(i==j):
			flag+=1
			count.append(flag)
print(count)

	
