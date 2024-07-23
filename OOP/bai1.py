class Sp():
    class_var = "Class Variable"

    def __init__(self, ten: str, gia: float, soluong=0):
        self.ten = ten
        self.gia = gia
        self.soluong = soluong

        # kiểm tra điều kiện thuộc tính
        assert gia >= 1.5

    def __tinhtoan__(self):
        return self.gia * self.soluong
    
    @staticmethod
    def my_static_method(x, y):
        return x + y
    
    # so sánh staticmethod và classmethod
    @staticmethod
    def static_method():
        return "I am a static method"

    @classmethod
    def class_method(cls):
        return f"I am a class method and I can access: {cls.class_var}"

# khởi tạo class con
class Sp2(Sp):
    def __init__(self, ten: str, gia: float, soluong=0, options="abc"):
        super().__init__(ten, gia, soluong)
        self.options = options
        self.__luong = 5000

    @property
    def luong(self):
        return self.__luong
    
    @luong.setter
    def luong(self, value):
        if value > 0:
            self.__luong = value
        else:
            raise ValueError("Lương phải lớn hơn 0")

    # Ghi đè phương thức __tinhtoan__
    def __tinhtoan__(self):
        return (self.gia * self.soluong) * 0.9  # Giảm giá 10%

class Sp3(Sp):
    def __init__(self, ten: str, gia: float, soluong=0, discount=0.8):
        super().__init__(ten, gia, soluong)
        self.discount = discount

    # Ghi đè phương thức __tinhtoan__
    def __tinhtoan__(self):
        return (self.gia * self.soluong) * self.discount  # Áp dụng mức giảm giá tùy chỉnh

# Sử dụng tính đa hình
def tinh_toan_tong(doi_tuong_sp):
    return doi_tuong_sp.__tinhtoan__()

# Khởi tạo các đối tượng của các lớp khác nhau
sp1 = Sp("Sản phẩm 1", 2.0, 10)
sp2 = Sp2("Sản phẩm 2", 3.0, 5)
sp3 = Sp3("Sản phẩm 3", 4.0, 2)

# Tính toán tổng tiền bằng cách sử dụng tính đa hình
print(f"Tổng tiền của {sp1.ten}: {tinh_toan_tong(sp1)}")  # Output: 20.0
print(f"Tổng tiền của {sp2.ten}: {tinh_toan_tong(sp2)}")  # Output: 13.5
print(f"Tổng tiền của {sp3.ten}: {tinh_toan_tong(sp3)}")  # Output: 6.4
