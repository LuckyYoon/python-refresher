import numpy as np

# Problem 1
print("#1")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("sum: ", a + b)
print("difference: ", a - b)

# Problem 2
print("\n", "#2")

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("sum: ", a + b)
print("difference: ", a - b)

# Problem 3
print("\n", "#3")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("dot: ", np.dot(a, b))

# Problem 4
print("\n", "#4")

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])

print("product: ", np.dot(a, b))

# Problem 5
print("\n", "#5")

a = np.array([1, 1, 2])

print("magnitude: ", np.linalg.norm(a))

# Problem 6
print("\n", "#6")

a = np.array([[1, 2], [3, 4]])

print("transpose: ", a.T)
