"""
Bài Tập 5: Quản Lý Nhân Viên
Yêu cầu:

Tạo lớp Employee với các thuộc tính name, position, và salary.
Tạo lớp con Manager và Developer kế thừa từ Employee:
Manager có thêm thuộc tính team_size (số lượng nhân viên quản lý).
Developer có thêm thuộc tính programming_languages (danh sách các ngôn ngữ lập trình).

"""

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, position, salary, team_size):
        super().__init__(name, position, salary)
        self.team_size = team_size

    def __str__(self):
        return super().__str__() + f", Team Size: {self.team_size}"

class Developer(Employee):
    def __init__(self, name, position, salary, programming_languages):
        super().__init__(name, position, salary)
        self.programming_languages = programming_languages

    def __str__(self):
        return super().__str__() + f", Programming Languages: {', '.join(self.programming_languages)}"
