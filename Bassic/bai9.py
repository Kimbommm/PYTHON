#Viết chương trình tạo ra 1 list có n phần tử, các phần tử là số ngẫu nhiên từ 1 - 30
#Viết chương trình nhập tay các phần tử của list
#Viết chương trình in ra các phần tử nhỏ hơn 10 và vị trí index của phần tử đó
#Viết chương trình bình phương các phần tử trong list vừa tạo
#Tính kết quả các biểu thức toán học trong chuỗi string

import random
import math

def random_list(n):
    list_of_random_integer = [random.randint(1,30) for _ in range(n)]
    return list_of_random_integer

def not_auto_List(n):
    user_input_List = []
    for i in range(n):
        value = int(input(f"Nhập giá trị phần tử tại vị trí thứ {i + 1}: "))
        user_input_List.append(value)
    return user_input_List

def value10_and_index(auto_List):
    result = []
    for i, value in enumerate(auto_List):
        if value < 10:
            result.append((i, value))
    return result

def vonglap_binhphuong(old_list):
    new_list = []
    for value in old_list:
        new_list.append(value ** 2)
    return new_list

def binhphuong_value(old_list):
    new_list = [value2 ** 2 for value2 in old_list]
    return new_list

def calculate_expression(question):
    #xóa khoảng trắng -> strip()
    #xóa dấu = -> replace()
    expression = question.replace("=", "").strip()

    #sử lí sqrt
    if "sqrt" in expression:
        expression = expression.replace("sqrt", "math.sqrt")
    
    #sau cùng dùng eval để tính toán các giá trị toán học trong string
    return eval(expression)


n = int(input("Nhập số lượng phần tử có trong list: "))

list = random_list(n)
print (f"danh sách các số ngẫu nhiên trong list: {list}")

vl10_and_index = value10_and_index(list)
for index, value in vl10_and_index:
    print(f"Phần tử nhỏ hơn 10 được tìm thấy tại vị trí {index}: {value}")

# list2 = not_auto_List(n)
# print (f"Nhập tay list: {list2}")

list3 = binhphuong_value(list)
print (f"Danh sách các phần tử bình phương theo cách 2: {list3}")

question = ["1 + 2 + 3 =","5 * 10 =","sqrt(16) =","12 % 2 =","5 // 2 ="]
for q in question:
    result = calculate_expression(q)
    print(f"Kết quả của '{q}' là: {result}")


