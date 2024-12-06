print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

class Circle(object):
    # Hàm khởi tạo __init__ để tạo đối tượng với bán kính r
    def __init__(self, r):
        self.radius = r
    
    # Phương thức tính diện tích
    def area(self):
        return self.radius ** 2 * 3.14

# Tạo đối tượng Circle với bán kính 2
aCircle = Circle(2)

# In ra diện tích của Circle
print(aCircle.area())
