"""
Bài Tập 3: Quản Lý Ngân Hàng
Yêu cầu:

Tạo lớp Account với các thuộc tính account_number và balance.
Tạo các phương thức:
deposit(amount): Thêm tiền vào tài khoản.
withdraw(amount): Rút tiền từ tài khoản nếu đủ số dư.
__str__(): Trả về thông tin tài khoản (số tài khoản và số dư).
"""

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance}"
