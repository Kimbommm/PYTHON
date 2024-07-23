#KIỂU DỮ LIỆU DICT
# Tạo từ điển rỗng
my_dict = {}

# Tạo từ điển với các cặp khóa-giá trị
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Truy cập giá trị bằng khóa
name = my_dict["name"]  # Alice
print (name)

# Truy cập một khóa không tồn tại
try:
    address = my_dict["address"]
except KeyError:
    print("KeyError: 'address' not found")
    
# Truy cập giá trị bằng phương thức get
age = my_dict.get("age")  # 25
print (age)

# Truy cập một khóa không tồn tại
address = my_dict.get("address")  # None
print(address)

# Truy cập một khóa không tồn tại với giá trị mặc định
address = my_dict.get("address", "Không tồn tại")
print(address) 

# Thêm một cặp khóa-giá trị mới
my_dict["email"] = "alice@example.com"

# Cập nhật giá trị của một khóa đã tồn tại
my_dict["age"] = 26

print("*" * 50)
# Sử dụng dict.keys() để lấy các khóa
keys = my_dict.keys()
print(keys)  # dict_keys(['name', 'age', 'city'])

# Chuyển đổi đối tượng view thành danh sách
keys_list = list(keys)
print(keys_list)  # ['name', 'age', 'city']

# Duyệt qua các khóa sử dụng dict.keys()
for key in keys:
    print(key)

print("*" * 50)
# Duyệt qua các giá trị
# dict.values(): Trả về một danh sách các giá trị trong từ điển.
for value in my_dict.values():
    print(value)

print("*" * 50)
# Duyệt qua các cặp khóa-giá trị
# dict.items(): Trả về một danh sách các cặp khóa-giá trị trong từ điển.
for key, value in my_dict.items():
    print(f"{key}: {value}")

# xóa 
# Sử dụng del
del my_dict["city"]

# Sử dụng phương thức pop
email = my_dict.pop("email")  # "alice@example.com"

print("*" * 50)
for key, value in my_dict.items():
    print(f"{key}: {value}")

print("*" * 50)
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

for person, details in nested_dict.items():
    print(f"{person}:")
    for key, value in details.items():
        print(f"  {key}: {value}")

#đếm tần suất kí tự xuất hiện trong chuỗi
text = "hello world"

# Khởi tạo một từ điển trống để lưu tần suất
frequency = {}

# Duyệt qua từng ký tự trong chuỗi
for char in text:
    if char in frequency:
        # Nếu ký tự đã tồn tại trong từ điển, tăng giá trị lên 1
        frequency[char] += 1
    else:
        # Nếu ký tự chưa tồn tại, khởi tạo giá trị bằng 1
        frequency[char] = 1

# In ra từ điển tần suất
print(frequency)

#đếm tần suất từ trong câu
sentence = "this is a test this is only a test"

# Khởi tạo một từ điển trống để lưu tần suất
word_frequency = {}

# Chia câu thành các từ
words = sentence.split()

# Duyệt qua từng từ trong danh sách
for word in words:
    if word in word_frequency:
        # Nếu từ đã tồn tại trong từ điển, tăng giá trị lên 1
        word_frequency[word] += 1
    else:
        # Nếu từ chưa tồn tại, khởi tạo giá trị bằng 1
        word_frequency[word] = 1

# In ra từ điển tần suất từ
print(word_frequency)
