def binary_search(mylist,key):
	low=0
	high=len(mylist)-1
	while low<=high:
		mid=(low+high)//2
		if mylist[mid]==key:
			return mid
		elif key>mylist[mid]:
			low=mid+1
		else:
			high=mid-1
	return -1

mylist = list(map(int,input().split()))
mylist.sort()
print(mylist)

key = int(input("Enter the number to search: "))
x = binary_search(mylist,key)
print(x)
if x == -1:
	print(key,"is not present in the list")
else:
	print("The Element ",key," is found at position",x+1)








