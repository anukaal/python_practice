s=0
num=int(input('Enter the number: '))
while(num!=0):
	temp=num%10
	s=s+temp
	num=num/10
print('The sum of digits : ', s)