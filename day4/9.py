import numpy as np
# 1
dtype1 = [('name', 'U10'), ('age', 'i4'), ('weight', 'f4')]
people = np.array([('Alice', 25, 55.5),
                   ('Bob', 30, 85.0),
                   ('Charlie', 22, 68.0)], dtype=dtype1)

sorted_people = np.sort(people, order='age')
print("Sorted by Age:\n", sorted_people)

# 2
dtype2 = [('x', 'i4'), ('y', 'i4')]
points = np.array([(1, 2), (4, 6), (7, 8)], dtype=dtype2)

p1=points[0]
p2=points[1]

distance=np.sqrt((p2['x']-p1['x'])**2 + (p2['y']-p1['y'])**2)
print(f"Distance between points {p1} and {p2}: {distance}")

