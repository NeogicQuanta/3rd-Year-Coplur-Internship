import numpy as np

a = np.array([1, 2, 3])
b = np.array([[4, 5, 6], [7, 8, 9]])

c = np.reshape(a, [1, 3])
print(np.concatenate((c, b)))
