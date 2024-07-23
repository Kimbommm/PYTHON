# # vòng lặp for
# # chạy đến giá trị cận liền kề

# for i in range(1,10):
#     print (i) # 1 - 9

# #chạy ngược lại
# for j in range(10,1,-1):
#     print (j) # 10 - 2

#Nhập vào 1 số n và tính tổng từ 1 đến 5 cộng với số n
# n = int(input("Nhap vao so n: "))
# if n % 2 == 0:
#     for i in range(1,6):
#         n += i
#     print (n) 
# else:
#     print ("Khong tinh so le!")

#for continue và break
#xuất các số từ 1 đến 20 nhưng bỏ qua các số chia hết cho 3 và dừng vòng lặp khi tổng các số xuất ra
# lớn hơn 15
# sum = 0
# for i in range(1,21):
#     if i % 3 == 0:
#         continue
#     if sum + i > 15: 
#         break
#     sum += i
#     print(i)
#     print(f"sum = {sum}")

#tính giai thừa của 1 số được nhập từ bàn phím -> bằng vòng lặp

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result

# def sum_of_factorials(n):
#     total_Sum = 0
#     for i in range(1, n + 1):
#         total_Sum += factorial(i)
#     return total_Sum

# n = int(input("Nhap vao n: "))
# print(f"Tổng các giai thừa từ 1 đến {n} là {sum_of_factorials(n)}")

# #tìm ước chung của 1 số sử dụng vòng lặp for
# def find_divisors(n):
#     divisors = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             divisors.append(i)
#     return divisors
# n = int(input("Nhap vao n: "))
# print(f"Các ước của {n} là: {find_divisors(n)}")

#VIẾT CHƯƠNG TRÌNH KIỂM TRA 1 SỐ CÓ PHẢI LÀ SỐ HOÀN THIỆN HAY KHÔNG
#KIỂM TRA SỐ HOÀN THIỆN TRONG ĐOẠN 1 - 1000
#cách 1: cơ bản
arrNumber = []
for number in range(1,1001):
    s = 0
    for i in range(1,number):
        if number % i == 0:
            s += i
    if s == number:
        arrNumber.append(number)
print(f"Cac so hoan thien trong doan tu 1 - 1000: {arrNumber}")    

#cách 2:
def is_perfect_number(n):
    # Hàm kiểm tra xem một số có phải là số hoàn hảo hay không
    if n < 2:
        return False
    sum_of_divisors = 1  # Bắt đầu với 1 vì 1 là ước số của mọi số
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum_of_divisors += i
            if i != n // i:  # Tránh đếm lại số ước nếu i là căn bậc hai của n
                sum_of_divisors += n // i
    return sum_of_divisors == n

def find_perfect_numbers(limit):
    # Hàm tìm các số hoàn hảo trong khoảng từ 1 đến limit
    perfect_numbers = []
    for num in range(1, limit + 1):
        if is_perfect_number(num):
            perfect_numbers.append(num)
    return perfect_numbers

# Sử dụng hàm để tìm các số hoàn hảo trong khoảng từ 1 đến 10000
limit = 10000
perfect_numbers = find_perfect_numbers(limit)
print(f"Các số hoàn hảo trong khoảng từ 1 đến {limit} là: {perfect_numbers}")
