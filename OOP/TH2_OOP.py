"""
Bài Tập 2: Định Nghĩa Lớp Hình Học
Yêu cầu:

Tạo một lớp trừu tượng Shape với các thuộc tính trừu tượng area và perimeter.
Tạo lớp con Circle và Rectangle kế thừa từ Shape:
Circle có thuộc tính radius, tính diện tích và chu vi hình tròn.
Rectangle có thuộc tính width và height, tính diện tích và chu vi hình chữ nhật.
"""
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
