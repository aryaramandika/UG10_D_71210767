a = int(input("Harga makanan sebesar Rp"))
b = int(input("Harga snack sebesar Rp"))
c = int(input("Harga minuman sebesar Rp"))
d = int(input("Uang yang anda bawa sebesar Rp"))
print("Total yang harus anda bayar sebesar Rp",a+b+c)
if (d == a+b+c):
    print("Uang anda pas! Tidak ada kembalian dan utang :D")
elif (d < a+b+c):
    print("Uang Anda kurang! Anda memiliki utang sebesar Rp",(a+b+c)-d)
else:
    (d > a+b+c)
    print("Anda memiliki kembalian sebesar Rp",d-(a+b+c))