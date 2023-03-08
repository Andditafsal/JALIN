nomor_awal = int(input('Masukan nomer awal:'))
nomor_akhir = int(input('Masukan nomer akhir:'))

for angka in range(nomor_awal, nomor_akhir):
    if angka % 3 == 0:
        print("bilangan kelipatan")
        print(angka, angka **2)
    else:
        print(" bukan bilangan kelipatan")
        print(angka, angka -1)
