import numpy as np

# love = "S"

"""
try:
    a = np.array([1, 2, 3, 4, 5], dtype="Flt")
    print(a)
except ValueError as e:
    print("Error:", e)
"""


"""
numpy functions
numpy.array: Create an array
numpy.zeros: Create an array filled with zeros
numpy.ones: Create an array filled with ones
numpy.arange: Create an array with a range of values
numpy.linspace: Create an array with evenly spaced values
numpy.random: Generate random numbers
numpy.mean: Calculate the mean of an array
numpy.sum: Calculate the sum of an array
numpy.reshape: Reshape an array
numpy.transpose: Transpose an array
numpy.concatenate: Concatenate two or more arrays
"""


print(np.array([[1, 2, 3], [4, 5, 6]]))

a = np.array([[1, 2, 3], [4, 5, 6]], order="F")
print(a)

print(np.linspace(0, 5, 10, endpoint=False, dtype=float, retstep=True))

# Random

print(np.random.rand(2, 3))

# Empty
print(np.empty((2, 3)))

# fill all with same value
print(np.full((2, 3), 7))


# Create a 2D array with a specific data type
a = np.array([[1, 2], [3, 4]], dtype=np.float64)
print(a[0, 0])
