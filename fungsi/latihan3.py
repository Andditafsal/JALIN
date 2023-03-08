#fungsi menampilkan deret

def deret(n):
    for x in range(1,  n):
        x +=1
        print(x **2)

n =int(input('Masukan nilai'))
deret(n)               