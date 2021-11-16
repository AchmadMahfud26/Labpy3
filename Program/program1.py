modalawal = 100000000
for i in range(1, 9):
    if (i >= 1 and i <= 2):
        b = modalawal * 0
        print("Laba Bulan ke", i, "=",b)
    if (i >= 3 and i <= 4):
        c = modalawal * 0.01
        print("Laba Bulan ke", i, "=",c)
    if (i >= 5 and i <= 7):
        d = modalawal * 0.05
        print("Laba Bulan ke", i, "=",d)
    if (i == 8):
        e = modalawal * 0.03
        print("Laba Bulan ke", i, "=",e)
total = b + c + d + e
print("\nTotal =", total)


    