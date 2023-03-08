umur = int(input('Masukan umur anda:'))
if umur < 10:
    print("Anda Menghitung luas persegi panjang")
    panjang = int (input ("Masukan panjang :"))
    lebar = int(input("Masukan lebar :"))
    luas = panjang * lebar
    print("Luas persegi adalah {0} ".format(luas))
else:
    print("Anda Menghitung volume persegi panjang")
    panjang = int (input ("Masukan panjang :"))
    lebar = int(input("Masukan lebar :"))
    tinggi = int(input("Masukan tinggi :"))
    volume = panjang * lebar * tinggi
    print("volume persegi adalah {0} ".format(volume))