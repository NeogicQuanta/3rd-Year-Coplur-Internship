import numpy as np

# swap using arr[i], arr[j] = arr[j], arr[i]

# swapping 2d array rows:: arr[[0, 3], :] = arr[[3, 0], :]

# swapping 3d array rows:: arr[rows, column, depth=[0,2]] = arr[rows, column, depth=[2,0]]

# np.isnan(arr) returns list of indices where the value is nan
# to convert nan values to zero, use np.nan_to_num(arr)
arr = np.array([1, 2, np.nan, 4, np.nan, 6])
print("Original array:")
print(arr)

print(arr[~np.isnan(arr)])
print(np.nan_to_num(arr, copy=False, nan=0.0))


# I/O operations

# np.loadtxt('file.txt') loads data from a text file
# np.savetxt('file.txt', arr) saves data to a text file
# np.save('file.npy', arr) saves data to a binary file
# np.load('file.npy') loads data from a binary file
# np.savez('file.npz', arr1=arr1, arr2=arr2) saves multiple arrays to a binary file
# np.load('file.npz') loads multiple arrays from a binary file
# np.genfromtxt('file.txt') loads data from a text file with missing values
# np.savetxt('file.txt', arr, delimiter=',') saves data to a text file with a delimiter
# np.savez_compressed('file.npz', arr1=arr1, arr2=arr2) saves multiple arrays to a compressed binary file


# CSV operations
# np.genfromtxt('file.csv', delimiter=',') loads data from a CSV file
# np.savetxt('file.csv', arr, delimiter=',') saves data to a CSV file


# Solving linear equations
# np.linalg.solve(A, b) solves the linear equation Ax = b

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([5, 6])
solution = np.linalg.solve(arr1, arr2)
print("Solution to the linear equation:")
print(solution)


# np.linalg.inv(arr) returns the inverse of a matrix
# np.dot(arr1, arr2) returns the dot product of two matrices
# np.cross(arr1, arr2) returns the cross product of two vectors


import matplotlib.pyplot as plt

# Plotting a simple graph using matplotlib
"""x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sine Wave")
plt.legend(["Sine Wave"])
plt.show()
"""

# Bar Graph
"""
x = ["Category 1", "Category 2", "Category 3"]
y = [10, 20, 15]

plt.bar(x, y)
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Graph")
plt.show()
"""

# Histogram
"""data = np.random.randn(1000)
plt.hist(data, bins=30, edgecolor='black')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()
"""

# Scatter Plot
"""x = np.random.rand(100)
y = np.random.rand(100)
plt.scatter(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot")
plt.show()"""

# Pie Chart
"""labels = ["Category A", "Category B", "Category C"]
sizes = [30, 40, 30]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
"""

# 3D Plotting

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)
ax.scatter(x, y, z)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.title("3D Scatter Plot")
plt.show()

# 3D Surface Plot
"""fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.title("3D Surface Plot")
plt.show()
"""
