for soal in range(0,10) :
    soal += 1
    if soal % 2 != 0 :
        while True : 
            print("No.",soal,"Jari-jari = ",soal)
            print("LUAS LINGKARAN = phi * r^2 ")
            luas_u = float(input("Masukkan Hasil Luas Lingkaran = "))
            luas = 3.14 * (soal ** 2)
            if luas_u != luas :
                print("Jawaban Anda Salah !!!")
                print("Hasil = ", luas)
            else :
                print("Jawaban Benar")
                break 
    else : 
        while True :
            print("No.",soal, "Sisi = ", soal)
            print("LUAS PERSEGI = sisi * sisi")
            luas_u = float(input("Masukkan Hasil Luas Persegi = "))
            luas = soal ** 2
            if luas_u != luas :
                print("Jawaban Anda Salah !!!")
                print("Hasil = ", luas)
            else :
                print("Jawaban Benar")
                break