import numpy as np

a = [10, 3, 20, 6, 17, 8]
print(np.max(a))

# 2
a = [10, 3, 20, 6, 17, 8]
print(np.min(a))

# 3
b = np.array([[4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(b.shape)

# 4
b = np.array([[4, 5, 6], [7, 8, 9], [10, 11, 12]])
for i in b:
    for j in i:
        print(j)
print(b[1, 2])

# 5
b = np.array([[4, 5, 6], [7, 8, 9]])
s = 0
for i in b:
    for j in i:
        s += j
print(s)

# 6
a = np.array([[10, 11, 12], [13, 14, 15]])
b = np.array([[4, 5, 6], [7, 8, 9]])
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
