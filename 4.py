import numpy as np

array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8, 9], [10, 11, 12]])

horizontal_stack = np.hstack((array1, array2))

print("Array 1:")
print(array1)

print("\nArray 2:")
print(array2)

print("\nHorizontal Stack:")
print(horizontal_stack)
