#vòng lặp while
#viết chương trình nhập vào số n từ bàn phím. n phải nằm trong khoảng 1 đến 99
#vòng lặp không biết trước được số lần lặp
#khi nào còn thỏa mãn điều kiện thì còn lặp
# n = int(input("Nhap vao so 1 - 99: "))
# while n <= 0 or n > 99:
#     n = int(input("Nhap lai n, n chi duoc trong khoang tu 1 - 99: "))
# print(n)
            

#while - else
#Điều này có thể hữu ích trong một số trường hợp, chẳng hạn khi bạn muốn thực 
# hiện một hành động nào đó chỉ khi vòng lặp hoàn thành trọn vẹn.
# i = 0
# while i < 5:
#     print(f"i hiện tại là: {i}")
#     i += 1
# else:
#     print("Vòng lặp while đã kết thúc mà không gặp lệnh break.")

# j = 0
# while j < 5:
#     print(f"j hiện tại là: {j}")
#     if j == 3:
#         print("Gặp lệnh break")
#         break
#     j += 1
# else:
#     print("Vòng lặp while đã kết thúc mà không gặp lệnh break.")

#while true
# while True:
#     ten = input("Nhap ten: ")
#     diemTB = float(input("Nhap diem: "))
#     print(f"Hoc sinh {ten} co diem TB: {diemTB}")

#     if diemTB >= 5:
#         print("DAT")
#     else:
#         print("KHONG DAT")
#     HOI = input("Ban co muon tiep tuc chuong trinh(N or n de thoat): ")
#     if HOI == "N" or HOI == "n":
#         break

#tìm gcd(UCLN) của 2 số
def gcd(a,b):
    while b: #số b là số nhập vào khác 0, vòng lặp được chạy cho đến khi b = 0 tức false -> dừng
        a , b = b, a % b
    return a
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
print(f"GCD của {a} và {b} là: {gcd(a, b)}")