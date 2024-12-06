print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

class IOString:
    def __init__(self):
        self.str1 = ""  # Khởi tạo chuỗi rỗng

    def get_String(self):
        # Nhận chuỗi từ người dùng
        self.str1 = input("Nhập một chuỗi: ")

    def print_String(self):
        # In chuỗi đã nhập ở dạng chữ in hoa
        print(self.str1.upper())


# Kiểm tra chương trình
str1 = IOString()
str1.get_String()       # Nhập chuỗi từ người dùng
str1.print_String()     # In chuỗi ở dạng in hoa
