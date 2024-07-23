#LIST TRONG PYTHON
n = int(input("Nhập số phần tử của list: "))
lst = [0] * n
print(lst)

#kiểm tra chiều dài của list'
print(len(lst))

#kiểm tra kiểu loại của list'
print(type(lst))

#xuất ngược list
lst1 = [1,2,3,4,5]
for i in range(len(lst1) - 1, -1, -1):
    iteame = lst1[i]
    print(iteame,end= " ")
print()

#thay đổi phần tử -> bằng cách gọi ra và gán lại
lst1[4] = "thay"
print(lst1) 

#xóa phần tử theo vị trí index
del lst1[4]
print(lst1) 

#xóa phần tử dựa theo giá trị được chỉ định
lst1.remove(1)
print(lst1) 

# #xóa cả list
# del lst1
# print(lst1)

#tìm min, max
lst2 = [1,2,3,1,4,5]
min_value = min(lst2)
max_value = max(lst2)
print(min_value)
print(max_value)

#thêm phần tử vào cuối list
lst2.append(6)
print(lst2)

#đếm số lần xuất hiện của phần tử trong list
dem = lst2.count(1)
print(dem)

#đảo ngược list
lst2.reverse()
print(lst2)

#thêm phần tử vào vị trí được chỉ định
lst2.insert(2,100)
print(lst2)

#tìm vị trí index của phần tử (chỉ trả về giá trị tìm thấy đầu tiên)
# nếu giá trị k có trong list sẽ báo lỗi
index = lst2.index(1)
print(index)

#thêm 1 list khác nối vào list ban đầu ở vị trí cuối cùng
list3 = [9,9,9]
lst2.extend(list3)
print(lst2)

#reset list về list rỗng
list3.clear()
print(list3)

#sắp xếp
lst2.sort()
print(lst2)

#sắp xếp và gán được
kkk = [1,2,5,2]
kkk1 = sorted(kkk)
print(kkk1)

