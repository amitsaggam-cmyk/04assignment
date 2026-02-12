import numpy as np
#1

arr3 = np.arange(1, 37).reshape(6, 6)
sub_array = arr3[2:5, 1:4]
print("A2.1:\n", sub_array)

#2

arr4 = np.random.randint(1, 21, (5, 5))
border = np.concatenate([arr4[0, :], arr4[-1, :], arr4[1:-1, 0], arr4[1:-1, -1]])
print("A2.2 Border Elements:\n", border)