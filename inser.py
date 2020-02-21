def insertion_sort(mylist):
	for i in range(1,len(mylist)):
		currentElement=mylist[i]
		k=i-1
		while k>=0 and mylist[k]>currentElement:
			mylist[k+1]=mylist[k]
			k=k-1
		mylist[k+1]=currentElement
mylist=list(map(int,input().split()))
print('Element before sorting')
print(mylist)
insertion_sort(mylist)
print('Element after sorting')
print(mylist)