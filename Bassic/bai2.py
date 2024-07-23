import math
# #if else
# #chương trình kiểm tra điểm trung bình của 1 học sinh
# dtb = float(input("Nhap diem trung binh: "))
# """
# Trong điều kiện elif, không cần kiểm tra thêm điều kiện dtb < 9.0 vì nếu điều kiện này không đúng thì đoạn mã sẽ không vào khối elif đó.
# Tương tự, khi dtb không thỏa mãn điều kiện của khối elif trước đó, thì điều kiện kiểm tra dtb < 7.0 cũng không cần thiết vì nếu không thì
# nó đã bị loại trừ ở khối điều kiện trước.
# """
# if dtb >= 9.0:
#     print("Gioi")
# elif dtb >= 7.0: 
#     print("Kha")
# elif dtb >= 5.0:
#     print("Trung binh")
# else:
#     print("Yeu")

# print("*" *50)

# #chương trình kiểm tra năm nhuận
# nam = int(input("Nhap vao nam can kiem tra: "))

# if (nam % 4 == 0) and (nam % 100 != 0 or nam % 400 ==0):
#     print("Nam nhuan!")
# else: 
#     print("Khong nhuan!")

# print("*" *50)

# #chương trình kiểm tra 1 tháng có bao nhiêu ngày
# thang = int(input("Nhap vao thang: "))

# if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
#     print(f"Thang {thang} co 31 ngay!")
# elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
#     print(f"Thang {thang} co 30 ngay!")
# else:
#     nam = int(input("Nhap vao nam can kiem tra: "))

#     if (nam % 4 == 0) and (nam % 100 != 0 or nam % 400 ==0):
#         print(f"Thang {thang} co 29 ngay!")
#     else: 
#         print(f"Thang {thang} co 28 ngay!")
        
# #chương trình kiểm tra tháng thuộc quý mấy
# thang = int(input("Nhap vao thang: "))

# if thang in (1,2,3):
#     print(f"Thang {thang} thuoc quy 1")
# elif thang in (4,5,6):
#     print(f"Thang {thang} thuoc quy 2")
# elif thang in (7,8,9):
#     print(f"Thang {thang} thuoc quy 3")  
# elif thang in (10,11,12):
#     print(f"Thang {thang} thuoc quy 4")
# else:
#     print("Thang khong dung, xin kiem tra lai")

#chương trình tối ưu dựa theo công thức toán học
# thang = int(input("Nhap vao thang: "))

# if 1 <= thang <= 12:
#     quy = (thang - 1) // 3 + 1
#     print(f"Thang {thang} thuoc quy {quy}")
# else:
#     print("Thang khong dung, xin kiem tra lai")


# giải phương trình bậc 2 dạng ax^2 + bx + c = 0
import math

def giai_phuong_trinh_bac_hai(a, b, c):
    # Kiểm tra nếu a = 0 thì phương trình trở thành bậc nhất
    if a == 0:
        if b == 0:
            if c == 0:
                return "Phương trình vô số nghiệm."
            else:
                return "Phương trình vô nghiệm."
        else:
            x = -c / b
            return f"Phương trình có một nghiệm: x = {x}"
    
    # Tính delta
    delta = b**2 - 4*a*c

    # Kiểm tra giá trị của delta để xác định nghiệm của phương trình
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
    elif delta == 0:
        x = -b / (2*a)
        return x
    else:
        return None  # Phương trình vô nghiệm nếu delta < 0

# Nhập các hệ số a, b, c từ người dùng
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Gọi hàm để giải phương trình và in kết quả
ket_qua = giai_phuong_trinh_bac_hai(a, b, c)
if ket_qua:
    if isinstance(ket_qua, tuple):
        x1, x2 = ket_qua
        print(f"Nghiệm của phương trình là: x1 = {x1}, x2 = {x2}")
    elif isinstance(ket_qua, str):
        print(ket_qua)  # Trường hợp phương trình vô số nghiệm hoặc vô nghiệm
    else:
        x = ket_qua
        print(f"Nghiệm kép của phương trình là: x = {x}")
else:
    print("Phương trình vô nghiệm.")
