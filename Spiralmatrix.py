matrix = [[1,2,3,13],[4,5,6,14],[7,8,9,15],[10,11,12,16]]

print(matrix)  # Print the original matrix
row = len(matrix)  # Get the number of rows in the matrix
col = len(matrix[0])  # Get the number of columns in the matrix
mat=[]  # Initialize an empty list to store the spiral order

# Traverse the matrix to print each element
for i in range(row):
    for j in range(col):
        print(matrix[i][j])  # Print each element in the matrix

# Create a reversed version of the matrix for later use
print_reverse = [i[::-1] for i in matrix[::-1]]  # Reverse each row of the reversed matrix
print(print_reverse)  # Print the reversed matrix

# While there are still rows in the matrix
while matrix:
    # Print and remove the first row of the matrix
    mat += (matrix.pop(0))  # Add the first row to the result list

    # If there are still columns left in the matrix
    if matrix and matrix[0]:
        # Traverse the rightmost column from top to bottom
        for row in matrix:
            mat.append(row.pop())  # Remove and add the last element of each row

    # If there are still rows left in the matrix
    if matrix and matrix[0]:
        print("now reverse")  # Indicate the start of reversing the bottom row
        # Traverse the last row from right to left
        for row in matrix[-1][::-1]:  # The slice [::-1] reverses the row
            mat.append(row)  # Add each element to the result list
        matrix.pop()  # Remove the last row from the matrix

    # If there are still columns left in the matrix
    if matrix and matrix[0]:
        # Traverse the leftmost column from bottom to top
        for row in matrix[::-1]:  # The slice [::-1] reverses the order of rows
            mat.append(row.pop(0))  # Remove and add the first element of each row

    print(mat)  # Print the current state of the result list
    print(matrix)  # Print the current state of the matrix