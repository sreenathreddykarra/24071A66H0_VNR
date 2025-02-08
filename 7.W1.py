import numpy as np

matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

addition = np.add(matrix1, matrix2)
print("Matrix Addition:\n", addition)

subtraction = np.subtract(matrix1, matrix2)
print("Matrix Subtraction:\n", subtraction)

multiplication = np.multiply(matrix1, matrix2)
print("Matrix Multiplication (Element-wise):\n", multiplication)

dot_product = np.dot(matrix1, matrix2)
print("Matrix Dot Product:\n", dot_product)

transpose = np.transpose(matrix1)
print("Matrix Transpose:\n", transpose)
