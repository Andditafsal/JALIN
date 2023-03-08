umur = int(input('Masukan umur anda:'))
hargaTiket = 50000

if umur > 10:
    uang = int(input('Uang yang anda bawa : '))
    if hargaTiket == uang:
        print('Selamat datang di zoo :) ')
    elif hargaTiket < uang: 
        kembalian = uang - hargaTiket
        print("Uang kembalian = {0}".format(kembalian))
        print('Selamat datang di zoo')
    else:
        ('Uang anda tidak cukup')
else:
    print('Anda belum cukup umur')
