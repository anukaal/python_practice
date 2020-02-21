matrix = []
no_of_rows = int(input())
no_of_columns = int(input())

for rows in range(no_of_rows):
	matrix.append([])
	print(matrix)
	for columns in range(no_of_columns):
		element = int(input())
		matrix[rows].append(element)
		print(matrix[rows])
print(matrix)

sum=0
for k in range(len(matrix)):

	sum+=matrix[k][k]
print(sum)