import math 
# Định nghĩa biến xinchao và in ra giá trị của nó
xinchao = "Hello"
print(xinchao)

# Yêu cầu người dùng nhập giá trị cho biến i và in ra giá trị đó
i = input("Nhap vao gia tri cua bien: ")
print(i)

# In ra kiểu dữ liệu của biến i
print(type(i))

# Ép kiểu giá trị nhập vào
i_1 = int(input("Nhap vao gia tri cua bien: "))
print(type(i_1))

#Viết chương trình tính chu vi và diện tích hình tròn.Nhập vào từ bàn phím bán kính r
r = float(input("Nhap vao r: "))
chuvi = 2*r*math.pi
dientich = math.pi*(r**2)

print("Chu vi: " , chuvi)
print(f"Dien tich: {round(dientich,2)} ")