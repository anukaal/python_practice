matrix1 = []
no_of_rows1 = int(input())
no_of_columns1 = int(input())

for rows in range(no_of_rows1):
	matrix1.append([])
	print(matrix1)
	for columns in range(no_of_columns1):
		element = int(input())
		matrix1[rows].append(element)
print(matrix1)

matrix2 = []
no_of_rows2 = int(input())
no_of_columns2 = int(input())

for rows in range(no_of_rows2):
	matrix2.append([])
	print(matrix2)
	for columns in range(no_of_columns2):
		element = int(input())
		matrix2[rows].append(element)
print(matrix2)


result=[]
for i in range(no_of_rows1):
	result.append([])
	for j in range(no_of_columns1):
		mul = 0
		mul += matrix1[i][j]*matrix2[j][i]
		result[i].append(mul)
print(result)
