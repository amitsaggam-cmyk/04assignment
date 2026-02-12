# 1
arr8 = np.random.randint(1, 10, (3, 3))
row_add = np.array([1, 2, 3])
print("Broadcast Row Add:\n", arr8 + row_add)

# 2
arr9 = np.random.randint(1, 10, (4, 4))
col_sub = np.array([1, 2, 3, 4])
print("Broadcast Column Sub:\n", arr9 - col_sub.reshape(4, 1))