import numpy as np

# Tạo mảng NumPy từ danh sách Python
arr = np.array([1, 2, 3, 4, 5])
print(arr)  # [1 2 3 4 5]

# Tạo mảng 2D từ danh sách lồng nhau
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)

# Mảng toàn số 0
zeros = np.zeros((2, 3))
print(zeros)
# [[0. 0. 0.]
#  [0. 0. 0.]]

# Mảng toàn số 1
ones = np.ones((2, 3))
print(ones)
# [[1. 1. 1.]
#  [1. 1. 1.]]

# Mảng với các số ngẫu nhiên
random_int_array = np.random.randint(1,10,size=(2,3))
print(random_int_array)

# Mảng với các giá trị từ 0 đến 10, khoảng cách giữa các giá trị là 2
arange_arr = np.arange(0, 10, 2)
print(arange_arr)  # [0 2 4 6 8]

# Mảng với các giá trị từ 0 đến 1, chia đều thành 5 phần
linspace_arr = np.linspace(0, 1, 5)
print(linspace_arr)  # [0.   0.25 0.5  0.75 1.  ]

# các thuộc tính của mảng
print(arr.shape)  # (2, 3) - hình dạng mảng
print(arr.ndim)   # 2 - số chiều của mảng
print(arr.size)   # 6 - tổng số phần tử trong mảng
print(arr.dtype)  # int64 - kiểu dữ liệu của các phần tử trong mảng

# Cộng 2 vào từng phần tử
print(arr + 2)  # [3 4 5 6 7]

# Trừ 2 từ từng phần tử
print(arr - 2)  # [-1  0  1  2  3]

# Nhân từng phần tử với 2
print(arr * 2)  # [ 2  4  6  8 10]

# Chia từng phần tử cho 2
print(arr / 2)  # [0.5 1.  1.5 2.  2.5]

