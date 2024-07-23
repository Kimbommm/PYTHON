#Đệ quy

#TÍNH GIAI THỪA CỦA 1 SỐ
# n! = n x (n - 1)
# 5! = 5 X 4 X 3 X 2 X 1 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

#TÍNH FIBONACCI
# F(n)=F(n−1)+F(n−2)
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(6))  

#SỬ DỤNG VÒNG LẶP ĐỂ TÍNH GIAI THỪA 2 BÀI TOÁN TRÊN
def fibonacci_VONGLAP(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
print(fibonacci_VONGLAP(6))  

def factorial_VONGLAP(n):
    if n <= 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial_VONGLAP(5))

# xem biểu thức này
import math

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x

def is_fibonacci(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# Ví dụ
print(is_fibonacci(8))   # Kết quả: True
print(is_fibonacci(10))  # Kết quả: False


