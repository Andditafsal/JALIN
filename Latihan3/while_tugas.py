for y in range(0, 10):
    nomor = y + 1
    while True:
        if nomor %2 !=0:
            jari = nomor
            print("{0}.hitung luas lingkaran dengan jari jari {1}".format(nomor, jari))
            luas = 3.14 * jari * jari
        else:
            sisi = nomor
            print("{0}.hitung luas persegi dengan dengan sisi {1}".format(nomor, sisi))
            luas = sisi * sisi
        jawab = float (input("jawaban anda:"))
        if jawab == luas:
            break

