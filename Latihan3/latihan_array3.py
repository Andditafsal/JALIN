#daftar nilai dengan rentang  0 - 100
# tampilkan satu persatu nilai 
#jika nilai lebih dari kkm , tampilkan nilai {0} lebih dari kkm

nilai = [70, 85, 60, 30, 100]
kkm = 55
for x in nilai:
    if x > kkm:
        print("nilai {0} lebih dari kkm".format(x))
    else:
        print("nilai{0} kurang dari kkm".format(x))

