def duyet_ma_tran(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

def kich_thuoc_ma_tran(matrix):
    so_hang = len(matrix) # để xác định số hàng.
    so_cot = len(matrix[0]) # để xác định số cột
    return so_hang, so_cot

# Kiểm tra xem ma trận có phải là ma trận vuông hay không và in ra kích thước của ma trận
def is_square_matrix(matrix):
    so_hang, so_cot = kich_thuoc_ma_tran(matrix)
    return so_hang == so_cot

def tong_theo_chieu_ngang(matrix):
    for idx, hang in enumerate(matrix):
        tong_hang = sum(hang)  # Tính tổng của hàng
        print(f"Tổng hàng thứ {idx} = {tong_hang}")

def tong_theo_chieu_doc(matrix):
    tong_cot = [0] * len(matrix[0])  # Khởi tạo list để lưu tổng của mỗi cột
    
    for hang in matrix:
        for idx, cot in enumerate(hang):
            tong_cot[idx] += cot
    
    for idx, tong in enumerate(tong_cot):
        print(f"Tổng cột thứ {idx} = {tong}")

#Tính tổng đường chéo chính: Các phần tử có chỉ số hàng bằng chỉ số cột (matrix[i][i]).
def tong_duong_cheo_chinh(matrix):
    tong = 0
    for i in range(len(matrix)):
        tong += matrix[i][i]
    return tong

#Tính tổng đường chéo phụ: Các phần tử có chỉ số hàng cộng chỉ số cột bằng kích 
#thước của ma trận trừ 1 (matrix[i][n-i-1]).
def tong_duong_cheo_phu(matrix):
    tong = 0
    n = len(matrix)
    for i in range(n):
        tong += matrix[i][n-i-1]
    return tong

#cách tính tổng đường chéo chính và phụ cho ma trận không vuông
def tong_duong_cheo_chinh(matrix):
    tong = 0
    so_hang = len(matrix)
    so_cot = len(matrix[0])
    so_phan_tu = min(so_hang, so_cot)
    
    for i in range(so_phan_tu):
        tong += matrix[i][i]
    
    return tong

def tong_duong_cheo_phu(matrix):
    tong = 0
    so_hang = len(matrix)
    so_cot = len(matrix[0])
    so_phan_tu = min(so_hang, so_cot)
    
    for i in range(so_phan_tu):
        tong += matrix[i][so_cot - i - 1]
    
    return tong
#tìm phần tử lớn nhất và nhỏ nhất 
def tim_max_min(matrix):
    max_value = float('-inf')  # Khởi tạo giá trị lớn nhất là âm vô cùng
    min_value = float('inf')   # Khởi tạo giá trị nhỏ nhất là dương vô cùng
    
    for row in matrix:
        for element in row:
            if element > max_value:
                max_value = element
            if element < min_value:
                min_value = element
    
    return max_value, min_value

#tìm phần tử lớn thứ 2 và nhỏ thứ 2
def tim_phan_tu_thu_2(matrix):
    # Tạo danh sách chứa tất cả các phần tử của ma trận
    # => lúc này nó đã tách rời ra từng các phần tử
    elements = [element for row in matrix for element in row] #list comprehension
    
    # Loại bỏ các phần tử trùng lặp 
    #list: list là một kiểu dữ liệu trong Python dùng để lưu trữ một dãy các phần tử có thể trùng lặp và có thứ tự.
    #set: set là một kiểu dữ liệu trong Python, tương tự như danh sách (list), nhưng các phần tử trong set phải là
    # duy nhất (không trùng lặp) và không có thứ tự
    elements = list(set(elements))
    
    # Sắp xếp danh sách các phần tử
    elements.sort()
    
    # Kiểm tra nếu danh sách có ít nhất 2 phần tử
    if len(elements) < 2:
        return None, None  # Không có phần tử thứ hai lớn nhất hoặc nhỏ nhất
    
    # Phần tử nhỏ thứ hai và lớn thứ hai
    second_smallest = elements[1]
    second_largest = elements[-2]
    
    return second_smallest, second_largest

# Ma trận ví dụ
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Gọi hàm duyệt ma trận
duyet_ma_tran(matrix)

# Tính kích thước ma trận
so_hang, so_cot = kich_thuoc_ma_tran(matrix)
print(f"Kích thước của ma trận là: {so_hang} hàng x {so_cot} cột")

# Kiểm tra xem matrix có phải là ma trận vuông hay không
if is_square_matrix(matrix):
    print("Ma trận là ma trận vuông.")
else:
    print("Ma trận không phải là ma trận vuông.")

# Gọi hàm tính tổng theo chiều ngang và in ra vị trí index của hàng
tong_theo_chieu_ngang(matrix)

# Gọi hàm tính tổng theo chiều dọc và in ra kết quả
tong_theo_chieu_doc(matrix)

# Tính tổng đường chéo chính
tong_chinh = tong_duong_cheo_chinh(matrix)
print(f"Tổng đường chéo chính = {tong_chinh}")

# Tính tổng đường chéo phụ
tong_phu = tong_duong_cheo_phu(matrix)
print(f"Tổng đường chéo phụ = {tong_phu}")


# Tính tổng đường chéo chính không phải ma trận vuông
tong_chinh2 = tong_duong_cheo_chinh(matrix2)
print(f"Tổng đường chéo chính = {tong_chinh2}")

# Tính tổng đường chéo phụ không phải ma trận vuông
tong_phu2 = tong_duong_cheo_phu(matrix2)
print(f"Tổng đường chéo phụ = {tong_phu2}")

# Tìm phần tử lớn nhất và nhỏ nhất
max_value, min_value = tim_max_min(matrix)
print(f"Phần tử lớn nhất = {max_value}")
print(f"Phần tử nhỏ nhất = {min_value}")

# Tìm phần tử lớn thứ hai và nhỏ thứ hai
second_smallest, second_largest = tim_phan_tu_thu_2(matrix)
print(f"Phần tử nhỏ thứ hai = {second_smallest}")
print(f"Phần tử lớn thứ hai = {second_largest}")