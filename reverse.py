num=int(input('Enter the number: '))

while(num!=0):
	temp=num%10
	num=num/10
	print(temp, end=" ")
print('Reverse number is :', )