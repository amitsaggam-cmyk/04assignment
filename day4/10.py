# 1
import numpy.ma as ma
data=np.random.randint(1,21,(4,4))
masked1 = ma.masked_greater(data, 10)
print("Sum of Unmasked Elements:", masked1.sum())

# 2

data2=np.random.randint(1,20,(3,3))
diag_mask = np.eye(3, dtype=bool)
masked_arr=ma.masked_array(data2, mask=diag_mask)
mean_unmasked = masked_arr.mean()
masked_arr = masked_arr.filled(mean_unmasked)
print("Diagonal Replaced with Mean:\n", masked_arr)










