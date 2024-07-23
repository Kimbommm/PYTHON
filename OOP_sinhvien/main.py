# main.py

from student import Student

def main():
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

if __name__ == "__main__":
    main()
