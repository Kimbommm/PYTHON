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

# Tạo đối tượng Student
student = Student("Alice", "001")

# Thêm điểm số
student.add_grade(85)
student.add_grade(92)
student.add_grade(78)
student.add_grade(88)

# In thông tin sinh viên
print(student)  
# Output: Student: Alice, ID: 001, Average Grade: 85.75, Highest Grade: 92, Lowest Grade: 78

# Danh sách điểm số
print("Grades List:", student.grades_list())  
# Output: Grades List: [85, 92, 78, 88]

# Xóa một điểm số
student.remove_grade(78)
print("Grades List after removing 78:", student.grades_list())  
# Output: Grades List after removing 78: [85, 92, 88]

# Thử thêm điểm số âm để kiểm tra ngoại lệ
try:
    student.add_grade(-10)  # Sẽ gây ra ngoại lệ
except ValueError as e:
    print("Error:", e)  
# Output: Error: Grade cannot be negative

# Thử lấy điểm số cao nhất và thấp nhất
try:
    print("Highest Grade:", student.highest_grade)  # Output: Highest Grade: 92
    print("Lowest Grade:", student.lowest_grade)    # Output: Lowest Grade: 85
except ValueError as e:
    print("Error:", e)

# Thử lấy điểm số cao nhất và thấp nhất khi không có điểm số
empty_student = Student("Bob", "002")
try:
    print("Highest Grade:", empty_student.highest_grade)  # Sẽ gây ra ngoại lệ
except ValueError as e:
    print("Error:", e)  # Output: Error: No grades available

try:
    print("Lowest Grade:", empty_student.lowest_grade)  # Sẽ gây ra ngoại lệ
except ValueError as e:
    print("Error:", e)  # Output: Error: No grades available
