#Biểu thức chính quy và thư viện re
# làm cách này để tính các số trong chuỗi s = "abc123def45gh6"
import re

def extract_numbers_from_string(s):
    # Sử dụng regex để tìm tất cả các số trong chuỗi
    numbers = re.findall(r'\d+', s)
    
    # Chuyển các số từ dạng chuỗi sang dạng số nguyên
    numbers = [int(num) for num in numbers]
    
    return numbers

def sum_of_numbers_in_string(s):
    numbers = extract_numbers_from_string(s)
    return sum(numbers)

def average_of_numbers_in_string(s):
    numbers = extract_numbers_from_string(s)
    if numbers:
        return sum(numbers) / len(numbers)
    else:
        return 0

# Ví dụ
s = "abc123def45gh6"

numbers = extract_numbers_from_string(s)
print(f"Các số trong chuỗi: {numbers}")

sum_numbers = sum_of_numbers_in_string(s)
print(f"Tổng các số trong chuỗi: {sum_numbers}")

average_numbers = average_of_numbers_in_string(s)
print(f"Trung bình các số trong chuỗi: {average_numbers}")
