matrix = [[1,2,3,13],[4,5,6,14],[7,8,9,15],[10,11,12,16]]

print(matrix)
row = len(matrix)
col = len(matrix[0])
mat=[]

for i in range(row):
    for j in range(col):
        print(matrix[i][j])


print_reverse = [i[::-1] for i in matrix[::-1]]
print(print_reverse)
    
while matrix:
#print first row of the matrix
#    if matrix:
        mat += (matrix.pop(0))
 #   if matrix:
        for row in matrix:
            mat.append(row.pop())
        if matrix:
            print("now reverse")
            for row in matrix[-1][::-1]:
                mat.append(row)
            matrix.pop()
 #   if matrix:
        for row in matrix[::-1]:
            mat.append(row.pop(0))


        print(mat) 
        print(matrix)