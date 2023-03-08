def luas_segitiga(alas, tinggi): 
    return alas * tinggi / 2

hasil_luas = luas_segitiga(6, 3)
print('Hasil luas segitiga adalah {0}'.format(hasil_luas))

def persegi(sisi): 
    return sisi * sisi

hasil_persegi = persegi(5)
print('Hasil persegi adalah {0}'.format(hasil_persegi))

def trapesium(a, b, t):
    return a + b * t /2

hasil_trapesium = trapesium(5, 3, 4)
print('Hasil luas trapesium adalah {0}'.format(hasil_trapesium))