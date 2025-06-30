import numpy as np

a = np.array([1, 2, 3])
b = np.array([[4, 5, 6], [7, 8, 9]])
print(np.flip(a))
print(np.flip(b, axis=1))
print(np.flip(b, axis=0))
