print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

class StringManipulator:
    def reverse_words(self, s):
        # Tách các từ trong chuỗi, đảo ngược thứ tự và ghép lại thành chuỗi mới
        return ' '.join(reversed(s.split()))

# Kiểm tra chương trình
manipulator = StringManipulator()
print(manipulator.reverse_words("hello .py"))  # Output: '.py hello'
