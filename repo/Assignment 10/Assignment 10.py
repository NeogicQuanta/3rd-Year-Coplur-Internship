import numpy as np

# ques1
arr = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])
res = np.nan_to_num(arr, copy=True, nan=0)
print(res)

arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr1[(0, 2), :] = arr1[(2, 0), :]
print(arr1)
print()
arr1[:, (0, 2)] = arr1[:, (2, 0)]
print(arr1)
print()

# ques2
arr = np.zeros([2, 3, 4])
r = np.transpose(arr, (1, 2, 0))
print(r.shape)

# ques3
arr = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])
res = np.nan_to_num(arr, copy=True, nan=np.nanmean(arr))
print(res)

# ques4
arr = np.array([[6, -8, 73, -110], [12, -8, 0, 94]])
arr[arr < 0] = 0
print(arr)

# ques5,6,7
arr1 = np.array([[1, 2], [4, 5]])
arr2 = np.array([[7, 8], [10, 11]])
arr = np.concatenate((arr1, arr2))
print(arr)
print(np.average(arr))
print(np.mean(arr))
print(np.median(arr))
from scipy import stats

print(stats.mode(arr))

# ques8
arr1 = np.array([[1, -2, 3], [-1, 3, -1], [2, -5, 5]])
arr2 = np.array([9, -6, 17])
r = np.linalg.solve(arr1, arr2)
print(r)
a = np.linalg.inv(arr1)
res = np.dot(a, arr2)
print(res)

# ques9
import matplotlib.pyplot as plt

categories = ["SEM1", "SEM2", "SEM3"]
values = [8.70, 8.75, 8.85]
plt.bar(categories, values, color="blue")
plt.title("Semester Wise Marks")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()
