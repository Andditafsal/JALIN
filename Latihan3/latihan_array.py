# forever looping
# menampilkan menu
# 1. menu pertama
# 2. Menu kedua
# 3. Menu ketiga
# keluar
# ambil inputann dari user
# jika input 4 , keluar dari looping
# jika input 3, maka tampilkan menu ke tiga
# jika innput 2, maka tampilkann  menu ke dua
#jika input 1 ,maka tampilkan menu pertama

while True :
    print("Menu pertama")
    print("Menu kedua")
    print("Menu ketiga")
    menu = int(input('Pilih menu'))
    if menu ==1:
        print("Tampil menu pertama")
    elif menu ==2:
        print("Tampil menu kedua")
    elif menu ==3:
        print('Tampil menu ke tiga')
    else:
        print("keluar") 
        break