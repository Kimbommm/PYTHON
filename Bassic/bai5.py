#thư viện time
import time

start_time = time.time()
# Thực hiện một số công việc mà bạn muốn đo thời gian
print("Xin chao!")
end_time = time.time()

execution_time = end_time - start_time
print(f"Thời gian thực thi: {execution_time} giây")

start_time = time.monotonic()
# Thực hiện một số công việc mà bạn muốn đo thời gian
end_time = time.monotonic()

execution_time = end_time - start_time
print(f"Thời gian thực thi: {execution_time} giây")
#2 CÁCH TRÊN CÓ SỰ KHÁC NHAU


#dừng chương trình theo số giây chỉ định
print("Đang đợi...")
time.sleep(5)  # Dừng chương trình trong 5 giây
print("Đã hoàn thành đợi!")

#lấy ra số giờ hiện tại
current_time = time.strftime("%Y-%m-%d %H:%M:%S")
print(f"Thời gian hiện tại: {current_time}")

#lấy ra các phần tử giừo
current_time = time.localtime()
print(f"Thời gian hiện tại: {current_time}")
print(f"Thời gian hiện tại: {current_time.tm_year}")

# VIẾT CHƯƠNG TRÌNH NHẬP VÀO NĂM SINH, XUẤT RA NĂM NAY BẠN BAO NHIÊU TUỔI
namsinh = int(input("Nhập vào năm sinh: "))
tuoi = current_time.tm_year - namsinh
print(f"Năm nay bạn được {tuoi} tuổi.")
# CÓ ĐƯỢC NĂM SINH HIỆN TẠI, HÃY THỬ XUẤT RA NĂM BAO NHIÊU TUỔI BẠN ĐƯỢC 100 TUỔI
namduoc100tuoi = current_time.tm_year + (100 - tuoi)
print(f"Năm bạn được 100 tuổi là năm: {namduoc100tuoi}")