# Assignment 7:
# 1
arr10 = np.arange(1, 10).reshape(3, 3)
reshaped1 = arr10.reshape(1, 9)
reshaped2 = arr10.reshape(9, 1)
print("Reshaped (1,9):\n", reshaped1)
print("Reshaped (9,1):\n", reshaped2)

# 2
arr11 = np.random.randint(1, 20, (5, 5))
flattened = arr11.flatten()
reshaped_back = flattened.reshape(5, 5)
print("Flattened:\n", flattened)
print("Reshaped Back:\n", reshaped_back)