#STRING_CHUỖI

str = "string"

#kiểm tra độ dài chuỗi
print(len(str))

#duyệt chuỗi
for i in str:
    print(i)

#duyệt trên cùng 1 dòng
for i in str:
    print(i, end= " ")
print("\n")

#cộng chuỗi
str1 = "string1"
str2 = "string2"
str3 = str + " " +  str1 + " " + str2
print(str3)

#nhân chuỗi
print("*" * 50)

#kiểm tra chuỗi nhập vào có nằm trong chuổi hay không
name = "name,name1,name2"
# value = input("Nhập vào tên: ")
# if value in name:
#     print("CÓ!")
# else:
#     print("KHÔNG!")

#xuất chuỗi theo vị trí index
value2 = "123456789"
print(value2[3]) #xuất giá trị ở vị trí index = 3
print(value2[3:6]) #xuất giá trị ở vị trí index = 3 đến 5
print(value2[::-1]) #đảo ngược chuỗi

#sử dụng vòng lặp for xuất kí tự đầu và kí tự cuối của chuỗi (KHÔNG DÙNG INDEX)
value3 = "123456789"
print(len(value3))
for i in range(len(value3)):
    if i == 0 or i == len(value3) - 1:
        print(value3[i],end= " ")
print()
#các hàm xử lí string

#xóa kí tự ở 2 đầu.Nếu không truyền gì vào tức là xóa khoảng trống
value4 = "   123   "
xoa_value4 = value4.strip()
print(xoa_value4)

#xóa kí tự ở 2 đầu.Nếu truyền vào thì nó xóa tới khi gặp khoảng trắng
value5 = "***123*** ***"
xoa_value5 = value5.strip("*")
print(xoa_value5)

#đếm số lần xuất hiện của kí tự ->có thể kiểm tra trong đoạn nào bằng cách thêm chỉ số
value6 = "***123*** ***"
dem_value6 = value6.count("*")
print(dem_value6)

#hàm viết hoa kí tự đầu
value7 =  "abc"
print(value7.capitalize())

#thay thế chuỗi, nếu có chỉ số index phía sau thì thay đổi theo số lần
text = "Hello, World!"
new_text = text.replace("World", "Python")
print(new_text)