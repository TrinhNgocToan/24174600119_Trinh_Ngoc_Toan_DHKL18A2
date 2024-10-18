import math
#cho pt f(X) nhập vào x đưa ra kq
x=float(input("nhập giá trị x là: "))
f = (-x + math.sqrt(x ** 2 + 4)) / (x ** 4 + 1) ** Faction(1, 2)
# In kết quả
print(f"Diện tích xung quanh: {dien_tich_xq:.2f}")



import math

def calculate_function(x):
    numerator = -x + math.sqrt(x**2 + 4)
    denominator = math.sqrt(x**4 + 1)
    return round(numerator / denominator, 2)

# Nhập giá trị của x từ người dùng
x = float(input("Nhập giá trị của x: "))
result = calculate_function(x)

print(f"Giá trị của f(x) là: {result}")