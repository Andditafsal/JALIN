def luas_segitiga(alas, tinggi): 
    hasil = alas * tinggi / 2
    
    print('jawab =', hasil)

def persegi(sisi): 
    hasil = sisi * sisi
    print('jawab =', hasil)

def trapesium(a, b, t):
    hasil = a + b * t /2
    print('jawab = ', hasil)

while True:
    print('Soal')
    print('1.Segitiga')
    print('2.Persegi')
    print('3.trapesium')
    print('4.keluar')
    jawab = int(input('Masukan Soal :'))

    if jawab == 1:
        print('Hitung segitiga')
        alas = int(input('masukan alas :'))
        tinggi = int(input('masukan tinggi :'))
        segitiga = (alas * tinggi /2)
    elif jawab == 2:
        print('Hitung Persegi')
        sisi = int(input('masukan sisi :'))
        persegi = (sisi * sisi)
    elif jawab  == 3:
        print('Hitung trapesium')
        a = int(input('masukan a:'))
        b = int(input('masukan b:'))
        t = int(input('masukan t:'))
        trapesium = a + b * t /2