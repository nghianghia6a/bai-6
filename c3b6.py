print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

class Nguoi(object):
    # Phương thức mặc định của lớp Nguoi, trả về "Unknown"
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    # Phương thức của lớp Nam, trả về "Nam"
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    # Phương thức của lớp Nu, trả về "Nữ"
    def getGender(self):
        return "Nữ"

# Tạo đối tượng Nam và Nu
aNam = Nam()
aNu = Nu()

# In giới tính của đối tượng
print(aNam.getGender())  # Kết quả: Nam
print(aNu.getGender())   # Kết quả: Nữ
