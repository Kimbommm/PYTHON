"""
Bài Tập 7: Danh Sách Sinh Viên với Lớp Trừu Tượng
Yêu cầu:

Tạo lớp trừu tượng Person với các thuộc tính trừu tượng name và age.
Tạo lớp con Student và Teacher kế thừa từ Person:
Student có thêm thuộc tính student_id.
Teacher có thêm thuộc tính subject.
"""

from abc import ABC, abstractmethod

class Person(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def age(self):
        pass

class Student(Person):
    def __init__(self, name, age, student_id):
        self._name = name
        self._age = age
        self.student_id = student_id

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, ID: {self.student_id}"

class Teacher(Person):
    def __init__(self, name, age, subject):
        self._name = name
        self._age = age
        self.subject = subject

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def __str__(self):
        return f"Teacher: {self.name}, Age: {self.age}, Subject: {self.subject}"
