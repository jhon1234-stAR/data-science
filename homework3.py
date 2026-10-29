import numpy as np

#matrix a 
matrix_a = np.arange(6).reshape(2, 3)

print("Matrix A:")
print(matrix_a)

# matrix b
matrix_b = np.arange(10, 16).reshape(2, 3)


print("Matrix B:")
print(matrix_b)

# Option A: Using the '+' operator
matrix_adding = matrix_a + matrix_b

matrix_sum = np.add(matrix_a, matrix_b)

print("Result of Matrix Addition (A + B):")
print(matrix_adding)
