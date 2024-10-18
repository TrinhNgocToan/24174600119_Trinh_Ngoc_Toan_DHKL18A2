import math

# Định nghĩa hằng số pi
pi = 3.14

# Nhập bán kính và chiều cao từ bàn phím
bankinh = float(input("Nhập bán kính của khối trụ: "))
chieucao = float(input("Nhập chiều cao của khối trụ: "))

# Tính diện tích xung quanh
dien_tich_xq = 2 * pi * bankinh * chieucao

# Tính diện tích toàn phần
dien_tich_toanphan = 2 * pi * bankinh * (bankinh + chieucao)

# Tính thể tích
the_tich = pi * bankinh**2 * chieucao

# In kết quả
print(f"Diện tích xung quanh: {dien_tich_xq:.2f}")
print(f"Diện tích toàn phần: {dien_tich_toanphan:.2f}")
print(f"Thể tích: {the_tich:.2f}")