import numpy as np

# Problem 1
print("#1", end=" ")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("sum: \n", a + b)
print("difference: \n", a - b)

# Problem 2
print("\n", "#2", end=" ")

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("sum: \n", a + b)
print("difference: \n", a - b)

# Problem 3
print("\n", "#3", end=" ")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("dot: \n", np.dot(a, b))

# Problem 4
print("\n", "#4", end=" ")

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])

print("product: \n", np.dot(a, b))

# Problem 5
print("\n", "#5", end=" ")

a = np.array([1, 1, 2])

print("magnitude: \n", np.linalg.norm(a))

# Problem 6
print("\n", "#6", end=" ")

a = np.array([[1, 2], [3, 4]])

print("transpose: \n", a.T)
