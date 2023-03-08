#predikat dari nilai
#nilai > 90 A
#90> nilai > 70 B
#70>nilai, c

def predikat(nilai):
    if nilai >90:
        return "A"
    elif nilai >70:
        return "B"
    else:
        return "C"

print(predikat(65))
print(predikat(89))
print(predikat(34))