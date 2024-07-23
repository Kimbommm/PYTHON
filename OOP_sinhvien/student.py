# student.py

from abstract_student import AbstractStudent

class Student(AbstractStudent):
    """Lớp Student triển khai các phương thức và thuộc tính từ lớp cơ sở trừu tượng."""

    def __init__(self, name, student_id): 
        super().__init__(name, student_id)
        self._grades = []

    @property
    def grades(self):
        """Thuộc tính đại diện cho danh sách điểm số."""
        return self._grades

    @property
    def average_grade(self):
        """Tính điểm trung bình của các điểm số."""
        return sum(self._grades) / len(self._grades) if self._grades else 0

    def add_grade(self, grade):
        """Thêm điểm số vào danh sách điểm."""
        if grade >= 0:  # Kiểm tra điểm số hợp lệ
            self._grades.append(grade)
        else:
            raise ValueError("Grade cannot be negative")

    def remove_grade(self, grade):
        """Xóa một điểm số khỏi danh sách điểm."""
        if grade in self._grades:
            self._grades.remove(grade)
        else:
            raise ValueError("Grade not found in the list")

    @property
    def highest_grade(self):
        """Trả về điểm số cao nhất."""
        if self._grades:
            return max(self._grades)
        raise ValueError("No grades available")

    @property
    def lowest_grade(self):
        """Trả về điểm số thấp nhất."""
        if self._grades:
            return min(self._grades)
        raise ValueError("No grades available")

    def grades_list(self):
        """Trả về danh sách các điểm số."""
        return self._grades

    def __str__(self):
        """Trả về chuỗi đại diện cho sinh viên."""
        return (f"Student: {self.name}, ID: {self.student_id}, "
                f"Average Grade: {self.average_grade:.2f}, "
                f"Highest Grade: {self.highest_grade if self._grades else 'N/A'}, "
                f"Lowest Grade: {self.lowest_grade if self._grades else 'N/A'}")
