# 1
matrix = np.random.randint(1, 10, (3, 3))
print("Matrix:\n", matrix)
print("Determinant:", np.linalg.det(matrix))
print("Inverse:\n", np.linalg.inv(matrix))
print("Eigenvalues:\n", np.linalg.eigvals(matrix))

# 2
m1 = np.random.randint(1, 10, (2, 3))
m2 = np.random.randint(1, 10, (3, 2))
print("Matrix Multiplication:\n", np.dot(m1, m2))