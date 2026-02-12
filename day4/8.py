import numpy as np
# 1
arr12 = np.random.randint(1, 20, (5, 5))
corners = arr12[[0, 0, -1, -1], [0, -1, 0, -1]]
print("Corners:\n", corners)

# 2
arr13 = np.random.randint(1, 20, (4, 4))
arr13[arr13 > 10] = 10
print("Boolean Indexed Array:\n", arr13)
