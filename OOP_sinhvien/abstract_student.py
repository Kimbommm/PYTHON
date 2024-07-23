# abstract_student.py

from abc import ABC, abstractmethod

class AbstractStudent(ABC):
    """Lớp cơ sở trừu tượng cho sinh viên."""

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    @property
    @abstractmethod
    def grades(self):
        """Thuộc tính trừu tượng đại diện cho danh sách điểm số."""
        pass

    @property
    @abstractmethod
    def average_grade(self):
        """Thuộc tính trừu tượng tính điểm trung bình của các điểm số."""
        pass

    @abstractmethod
    def add_grade(self, grade):
        """Thêm điểm số vào danh sách điểm."""
        pass

    @abstractmethod
    def remove_grade(self, grade):
        """Xóa một điểm số khỏi danh sách điểm."""
        pass

    @property
    @abstractmethod
    def highest_grade(self):
        """Thuộc tính trừu tượng trả về điểm số cao nhất."""
        pass

    @property
    @abstractmethod
    def lowest_grade(self):
        """Thuộc tính trừu tượng trả về điểm số thấp nhất."""
        pass

    @abstractmethod
    def grades_list(self):
        """Trả về danh sách các điểm số."""
        pass

    @abstractmethod
    def __str__(self):
        """Trả về chuỗi đại diện cho sinh viên."""
        pass
