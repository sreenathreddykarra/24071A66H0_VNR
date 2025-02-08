import numpy as np

random_matrix = np.random.randint(0, 10, (5, 5))

print("Random Matrix:")
print(random_matrix)

element = random_matrix[2, 3]
print("\nExtracted Element:")
print(element)
