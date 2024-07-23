class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value > 0:
            self._celsius = value
        else:
            raise ValueError("Temperature in Celsius must be greater than 0")

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

temp = Temperature(25)
print(temp.fahrenheit)  # Output: 77.0

# Thay đổi giá trị celsius thông qua setter
temp.celsius = 30
print(temp.fahrenheit)  # Output: 86.0

# Thử đặt giá trị không hợp lệ cho celsius
try:
    temp.celsius = -5  # Sẽ gây ra ngoại lệ
except ValueError as e:
    print(e)  # Output: Temperature in Celsius must be greater than 0
