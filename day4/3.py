# 1
a = np.random.randint(1, 10, (3, 4))
b = np.random.randint(1, 10, (3, 4))

print("Addition:\n", a + b)
print("Subtraction:\n", a - b)
print("Multiplication:\n", a * b)
print("Division:\n", a / b)

# 2
arr5 = np.arange(1, 17).reshape(4, 4)
print("Row-wise sum:", arr5.sum(axis=1))
print("Column-wise sum:", arr5.sum(axis=0))