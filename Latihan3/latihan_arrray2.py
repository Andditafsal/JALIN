# buat variabel array kosong []
# forever looping
# menampilkan menu
# 1. tambahkan antrian
# 2. panggil antrian
# 3. tampilkan antrian
# keluar
# ambil inputan dari user
# jika input 4 , keluar dari looping
# jika input 3, tampilkan variabel dari antrian
# jika innput 2, maka hapus orang pertama dari antrian
#jika input 1 ,maka tampilkan tampilkan antrian


antrian = []
while True:
    print("Menu")
    print("1.tambahkan antrian")
    print("2.panggil antrian")
    print("3.tampilkan antrian")
    print("4.keluar")
    menu = int(input("pilih menu"))

    if menu ==1 :
        nama = str(input("menambahkan nama :"))
        antrian.append(nama)
    elif menu ==2 :
        nama = antrian.pop(0)
        print(nama)
    elif menu ==3 :
        print(antrian)
    else: 
        break




