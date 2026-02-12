# 1
import numpy.ma as ma

masked1 = ma.masked_greater(np.random.randint(1, 20, (4, 4)), 10)
print("Sum of Unmasked Elements:", masked1.sum())

# 2
masked2 = ma.masked_array(np.random.randint(1, 20, (3, 3)))
masked2.mask = np.eye(3, dtype=bool)
mean_unmasked = masked2.mean()
masked2 = masked2.filled(mean_unmasked)
print("Diagonal Replaced with Mean:\n", masked2)