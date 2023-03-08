#while True:
    #print('hasil dari 1 + 1 adalah ?')
    #jwb_benar = 2
    #jwb_user = int(input('jawaban :'))
    #if jwb_benar == jwb_user:
        #break
#menggunakan wrepper looping while
## ambil inputan jari jari 
##hitung luas lingkaran 
##ambil inputan luas lingkaran dari user
## jika inputan sama dengan luas lingkaran
## maka keluar dari perulangan
##maka tampilkan yang benar

while True:
    jari = int(input("Masukan rummus jari-jari"))
    luas = 3.14 * (jari **2)
    luasInput = int(input('masukan hasil luas'))
    if luas == luasInput:
        print("jawaban anda benar")
        break
    else:
        print('jawaban yang benar adalah {0}'.format(luas))



