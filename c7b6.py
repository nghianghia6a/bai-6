print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

import math

class Circle:
    # Hàm khởi tạo __init__ để tạo đối tượng với bán kính r
    def __init__(self, r):
        self.radius = r
    
    # Phương thức tính diện tích
    def area(self):
        return math.pi * self.radius ** 2
    
    # Phương thức tính chu vi
    def circumference(self):
        return 2 * math.pi * self.radius

# Tạo đối tượng Circle với bán kính 5
circle = Circle(5)

# In diện tích và chu vi của Circle
print(f"Diện tích: {circle.area():.2f}")
print(f"Chu vi: {circle.circumference():.2f}")
