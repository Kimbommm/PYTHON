"""
Bài Tập 4: Hệ Thống Quản Lý Đơn Hàng
Yêu cầu:

Tạo lớp Order với các thuộc tính order_id, customer_name, và items (danh sách các mặt hàng với số lượng và giá).
Tạo các phương thức:
add_item(item_name, quantity, price): Thêm mặt hàng vào đơn hàng.
total_amount(): Tính tổng giá trị đơn hàng.
__str__(): Trả về thông tin đơn hàng (ID đơn hàng, tên khách hàng và tổng giá trị).
"""

class Order:
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = []

    def add_item(self, item_name, quantity, price):
        self.items.append({"item_name": item_name, "quantity": quantity, "price": price})

    def total_amount(self):
        return sum(item['quantity'] * item['price'] for item in self.items)

    def __str__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer_name}, Total Amount: {self.total_amount()}"
