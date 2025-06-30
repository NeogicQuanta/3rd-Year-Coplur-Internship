import numpy as np

# print(arr[0, 1, 2])
# a = np.zeros((2, 3, 4))
# print(a)

# print(arr.reshape(6, 3))

arr = np.array(
    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
)

padded_arr = np.pad(
    arr, pad_width=((1, 1), (1, 1), (1, 1)), mode="constant", constant_values=0
)
print(padded_arr)
