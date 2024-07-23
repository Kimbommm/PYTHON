"""
Bài Tập 6: Hệ Thống Đặt Vé
Yêu cầu:

Tạo lớp Ticket với các thuộc tính event_name, price, và quantity.
Tạo lớp Event với các thuộc tính event_name, tickets (danh sách các vé).
Tạo các phương thức cho lớp Event:
add_ticket(ticket): Thêm vé vào sự kiện.
total_revenue(): Tính tổng doanh thu từ việc bán vé.

"""

class Ticket:
    def __init__(self, event_name, price, quantity):
        self.event_name = event_name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

class Event:
    def __init__(self, event_name):
        self.event_name = event_name
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def total_revenue(self):
        return sum(ticket.total_price() for ticket in self.tickets)

    def __str__(self):
        return f"Event: {self.event_name}, Total Revenue: {self.total_revenue()}"
