#1.
import numpy as np
arr1_1 = np.random.randint(1, 21, (5, 5))
arr1_1[:, 2] = 1
print(arr1_1)

# 2
arr2 = np.arange(1, 17).reshape(4, 4)
np.fill_diagonal(arr2, 0)
print(arr2)