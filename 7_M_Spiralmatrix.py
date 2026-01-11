#Question: Print the elements of a matrix in spiral order.
# Example 1:
# Input: 
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
# Input: 
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7] 

matrix = [[3],[2]]
# matrix = [[1,2,3,13],[4,5,6,14],[7,8,9,15],[10,11,12,16]]

def spiralmatrix(matrix:list[list[int]]):
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


#----------------------------------------------
#My Soluiton
def matrixspiral(matrix: list[list[int]]) -> list[int]:
    output = []
    while matrix: # O(mn)

        # Step 1: pop the first row as it is
        output += matrix.pop(0)  # Make sure to add += or else the loop will reset

        # step 2: pop the last elements of the array
        if matrix and matrix[0]: #O(1)
            for i in range(len(matrix)): # O(m)
                output += [matrix[i].pop()]
                # output.append(matrix[i].pop())

        # step 3: pop the elements in the reverse order
        if matrix and matrix[-1]:
            last_row = matrix.pop()
            output += last_row[::-1]
            # output += matrix[-1][::-1]

        # step 4: first elements of all rows
        if matrix and matrix[0]:
            for i in range(len(matrix)): # O(m)
                output += [matrix[i].pop(0)]
                # output.append(matrix[i].pop(0))

        # #step 5: first remaining row
        # if matrix and matrix[0]:
        #     output += matrix.pop(0) 
        #We do not need a step 5 as the step five is same as step 1 adding a step 5 messes the start of new cycle

    return output

# Time complexity is O(mn) as we traverse through all the elements of the matrix
# Space complexity is O(1) as we are not using any extra space except output list



if __name__ == "__main__":
    # output =[]
    # print(len(matrix[0]))
    # print(matrix.pop(0))
    # print(matrix)
    # print(range(len(matrix)))
    # print(matrix[0].pop())
    # print(matrix[1].pop())
    # print(matrix)
    # print(matrix[-1])
    # print(matrix[::-1])
    # last_row = matrix.pop()
    # print(last_row)
    # output += last_row[::-1]
    # print(output)
    print(matrixspiral(matrix))
