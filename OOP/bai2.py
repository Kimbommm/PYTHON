from abc import ABC, abstractmethod

# Định nghĩa lớp trừu tượng
class HinhHoc(ABC):
    @abstractmethod
    def tinh_dien_tich(self):
        pass

    @abstractmethod
    def tinh_chu_vi(self):
        pass

# Lớp hình tròn kế thừa từ lớp trừu tượng HinhHoc
class HinhTron(HinhHoc):
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh

    def tinh_dien_tich(self):
        return 3.14 * self.ban_kinh ** 2

    def tinh_chu_vi(self):
        return 2 * 3.14 * self.ban_kinh

# Lớp hình chữ nhật kế thừa từ lớp trừu tượng HinhHoc
class HinhChuNhat(HinhHoc):
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)

# Hàm sử dụng tính đa hình
def in_thong_tin_hinh(hinh: HinhHoc):
    print(f"Dien tich: {hinh.tinh_dien_tich()}")
    print(f"Chu vi: {hinh.tinh_chu_vi()}")

# Khởi tạo các đối tượng của các lớp khác nhau
hinh_tron = HinhTron(5)
hinh_chu_nhat = HinhChuNhat(4, 6)

# Sử dụng tính đa hình để in thông tin
print("Thông tin hình tròn:")
in_thong_tin_hinh(hinh_tron)

print("\nThông tin hình chữ nhật:")
in_thong_tin_hinh(hinh_chu_nhat)
