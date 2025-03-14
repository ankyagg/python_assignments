import numpy as np


A = np.array([[2, 4, 6], [8, 10, 12]])
B = np.array([[1, 2, 3], [4, 5, 6]])

addition = A + B
subtraction = A - B
multiplication = A * B
division = A / B

print("Element-wise Addition:\n", addition)
print("Element-wise Subtraction:\n", subtraction)
print("Element-wise Multiplication:\n", multiplication)
print("Element-wise Division:\n", division)

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

dot_product = np.dot(vector1, vector2)
print("\nDot Product:", dot_product)

cross_product = np.cross(vector1, vector2)
print("Cross Product:\n", cross_product)
