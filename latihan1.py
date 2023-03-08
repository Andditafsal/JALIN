#perulangan x dari 30 - 0
#jika x habis dibagi 4 maka x dipangkatkan 2
#jika x habis di bagi 3, maka tidak ada proses
#jika x  kurang dari 5, maka hentikan perulangan
#jika semua kondisi tidak terpenuhi, tampilkan x



x = 30
while x > 0 :
    x -= 1
    if x <5 :
        break
    elif x %3 == 0:
        continue
    elif x %4 == 0:
        print(x ** 2)
    else:
        print(x)
