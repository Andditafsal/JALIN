hargaBarang = int(input('Masukan harga barang yang di beli :'))
jmlBarang = int(input('Maasukan jumalah barang yang akan di beli:'))

total = hargaBarang * jmlBarang

if total <100000:
    diskon = total * (30 / 100)
    bayar = total - diskon
    print('Selamat anda mendapatkan diskon 30%')
elif total <300000:
    diskon = total * (50 / 100)
    bayar = total - diskon
    print('Selamat anda mendapatkan diskon 50%')
else:
    print("Anda tidak mendapatkan potongan")
    print("Harga yang di bayar = {0}".format(total))
    
print("Harga yang di bayar = {0}".format(bayar))