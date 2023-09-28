print("Please enter the input in the following format (n m on the first line, followed by the matrix content):")

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []
for i in range(n):  
    matrix_item = input()
    
    if len(matrix_item) != m:
        print("Error: Rows must have consistent lengths.")
        print("Skipping this row.")
    else:
        matrix.append(matrix_item)

result = ""

for col in range(m):
    for row in range(n):
        char = matrix[row][col]

        if char.isalnum() or char.isspace():
            result += char
        else:
            result += ' '

result = ' '.join(result.split())

print("result : ",result)
