barang1 = input("Masukkan daftar belanja Anda : ")
list1 = barang1.title()
list2 = list1.split(",")
print("Daftar belanja :",list2)
barang2 = input("Masukkan barang yang ingin ditambahkan :")
list4 = barang2.upper()
list5 = barang2.title()
if list5 in list1 :
    print("Barang",list4,"sudah berada dalam daftar belanja.")
else:
    barang2 not in barang1
    list2.append(list4)
    print("Hasil penambahan pada daftar belanja :",list2)