print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

class HinhChunhat:
    # Hàm khởi tạo __init__ để tạo đối tượng với chiều dài và chiều rộng
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
    
    # Phương thức tính diện tích
    def dien_tich(self):
        return self.dai * self.rong

# Tạo đối tượng HinhChunhat với chiều dài 5 và chiều rộng 3
hcn = HinhChunhat(5, 3)

# In ra diện tích của Hình Chữ Nhật
print(hcn.dien_tich())
