#CÁC PHƯƠNG PHÁP TÌM GIÁ TRỊ LỚN NHẤT VÀ NHỎ NHẤT TRONG LIST
#Phương pháp 1: Duyệt danh sách
def find_max_min(nums):
    if not nums:
        return None, None  # Trường hợp danh sách rỗng

    max_val = float('-inf')
    min_val = float('inf')

    for num in nums:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return max_val, min_val


#Phương pháp 2: Sắp xếp danh sách và lấy giá trị
def find_max_min_sorted(nums):
    if not nums:
        return None, None  # Trường hợp danh sách rỗng

    sorted_nums = sorted(nums)
    max_val = sorted_nums[-1]
    min_val = sorted_nums[0]

    return max_val, min_val

#CÁC PHƯƠNG PHÁP TÌM GIÁ TRỊ LỚN THỨ 2 VÀ NHỎ THỨ 2 TRONG LIST
#Phương pháp 1: Duyệt danh sách
def find_second_largest_and_smallest(nums):
    if len(nums) < 2:
        return None, None  # Không đủ phần tử để tìm thứ hai

    max1, max2 = float('-inf'), float('-inf')
    min1, min2 = float('inf'), float('inf')

    for num in nums:
        # Tìm giá trị lớn thứ hai
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
        
        """
        Tình huống không có điều kiện num != max1
Giả sử không có điều kiện num != max1, tình huống sau có thể xảy ra:

Danh sách nums là [3, 3, 4, 4, 5, 5].
Khi num là 5 lần đầu tiên:
max1 sẽ được cập nhật thành 5.
max2 sẽ được cập nhật thành giá trị lớn nhất trước đó (ví dụ: 4).
Khi num là 5 lần thứ hai:
num > max2 vẫn đúng (vì 5 > 4).
Nếu không có điều kiện num != max1, max2 sẽ được cập nhật thành 5, 
làm sai lệch kết quả (vì cả max1 và max2 đều là 5).
        """
        # Tìm giá trị nhỏ thứ hai
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2 and num != min1:
            min2 = num

    return max2 if max2 != float('-inf') else None, min2 if min2 != float('inf') else None

# Phương pháp 2: Sắp xếp và lấy phần tử thứ hai từ đầu
def find_second_largest_and_smallest_sorted(nums):
    if len(nums) < 2:
        return None, None  # Không đủ phần tử để tìm thứ hai

    sorted_nums = sorted(nums)
    
    second_smallest = sorted_nums[1] if len(sorted_nums) > 1 else None
    second_largest = sorted_nums[-2]  # Phần tử lớn thứ hai từ cuối danh sách

    return second_largest, second_smallest

# Ví dụ sử dụng
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

max_val, min_val = find_max_min(nums)
print("Giá trị lớn nhất trong danh sách là:", max_val)  # Kết quả là 9
print("Giá trị nhỏ nhất trong danh sách là:", min_val)  # Kết quả là 1

max_val_sorted, min_val_sorted = find_max_min_sorted(nums)
print("Giá trị lớn nhất (sắp xếp) trong danh sách là:", max_val_sorted)  # Kết quả là 9
print("Giá trị nhỏ nhất (sắp xếp) trong danh sách là:", min_val_sorted)  # Kết quả là 1

second_largest, second_smallest = find_second_largest_and_smallest(nums)
print("Giá trị lớn thứ hai trong danh sách là:", second_largest)  # Kết quả là 6
print("Phần tử nhỏ thứ hai trong danh sách là:", second_smallest)  # Kết quả là 2

second_largest_sorted, second_smallest_sorted = find_second_largest_and_smallest_sorted(nums)
print("Giá trị lớn thứ hai (sắp xếp) trong danh sách là:", second_largest_sorted)  # Kết quả là 6
print("Phần tử nhỏ thứ hai (sắp xếp) trong danh sách là:", second_smallest_sorted)  # Kết quả là 2
