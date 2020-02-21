def selection_sort(mylist):
	for i in range(len(mylist)):
		k=i
		for j in range(i+1,len(mylist)):
			if(mylist[j]<mylist[k]):
				k=j
		if(k!=i):
			temp=mylist[i]
			mylist[i]=mylist[k]
			mylist[k]=temp
mylist = list(map(int,input().split()))
print("Element before sorting")
print(mylist)
selection_sort(mylist)
print('Element after sorting')
print(mylist)
