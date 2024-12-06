print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

class RomanToInteger:
    def roman_to_int(self, s):
        # Tạo từ điển lưu giá trị của các ký tự La Mã
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        
        # Lặp qua từng ký tự trong chuỗi La Mã
        for i in range(len(s)):
            # Nếu ký tự hiện tại nhỏ hơn ký tự tiếp theo, trừ đi giá trị của ký tự hiện tại
            if i > 0 and roman_values[s[i]] > roman_values[s[i - 1]]:
                int_val += roman_values[s[i]] - 2 * roman_values[s[i - 1]]
            else:
                # Ngược lại, cộng giá trị của ký tự hiện tại
                int_val += roman_values[s[i]]
        
        return int_val


# Kiểm tra chương trình
converter = RomanToInteger()
print(converter.roman_to_int("MMMMCMXLV"))  # Output: 4945
print(converter.roman_to_int("C"))          # Output: 100
