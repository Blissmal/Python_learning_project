def input_matrix(rows, cols):
    matrix = []
    print(f"Enter the elements of the {rows}x{cols} matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def subtract_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

def multiply_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = 0
            for k in range(len(matrix2)):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)
    return result

def transpose_matrix(matrix):
    transposed = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        transposed.append(row)
    return transposed

# Main program
rows1 = int(input("Enter the number of rows for matrix 1: "))
cols1 = int(input("Enter the number of columns for matrix 1: "))
matrix1 = input_matrix(rows1, cols1)

rows2 = int(input("Enter the number of rows for matrix 2: "))
cols2 = int(input("Enter the number of columns for matrix 2: "))
matrix2 = input_matrix(rows2, cols2)

print("\nMatrix 1:")
print_matrix(matrix1)
print("\nMatrix 2:")
print_matrix(matrix2)

if (rows1, cols1) != (rows2, cols2):
    print("Matrices must have the same dimensions for addition and subtraction.")
else:
    print("\nAddition:")
    print_matrix(add_matrices(matrix1, matrix2))

    print("\nSubtraction:")
    print_matrix(subtract_matrices(matrix1, matrix2))

if cols1 != rows2:
    print("Matrices cannot be multiplied. Number of columns of matrix 1 must be equal to the number of rows of matrix 2.")
else:
    print("\nMultiplication:")
    print_matrix(multiply_matrices(matrix1, matrix2))

print("\nTranspose of Matrix 1:")
print_matrix(transpose_matrix(matrix1))
print("\nTranspose of Matrix 2:")
print_matrix(transpose_matrix(matrix2))
