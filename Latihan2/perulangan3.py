#for <variable> in range <awal>, <akhir>
#for <variable> in range <awal>, <akhir>, <kelipatan>

for x in range(0, 12, 2):
    print(x)

for a in range(1, 12, 2):
    print(a)

print('LATIHAN')
for a in range(0, 20, 1):
    if a % 3 == 0 and a % 5 == 0 :
        print(a, a +3)
    elif a % 3 == 0 :
        print(a, a -3)
    else:
        print(a, a +1)
    