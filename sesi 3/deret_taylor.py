import math

# Nilai yang diketahui
a = 25
x = 26
h = x - a

# Nilai sebenarnya
nilai_asli = math.sqrt(x)

# Koefisien Taylor
c0 = 5
c1 = 1 / 10
c2 = -1 / 1000
c3 = 1 / 25000
c4 = -1 / 500000

# Menghitung P0 sampai P4
p0 = c0
p1 = p0 + c1 * h
p2 = p1 + c2 * h**2
p3 = p2 + c3 * h**3
p4 = p3 + c4 * h**4

# Menghitung galat absolut
print("Nilai sebenarnya =", nilai_asli)

print("P0 =", p0)
print("Galat P0 =", abs(nilai_asli - p0))

print("P1 =", p1)
print("Galat P1 =", abs(nilai_asli - p1))

print("P2 =", p2)
print("Galat P2 =", abs(nilai_asli - p2))

print("P3 =", p3)
print("Galat P3 =", abs(nilai_asli - p3))

print("P4 =", p4)
print("Galat P4 =", abs(nilai_asli - p4))

# Menentukan orde minimal
if abs(nilai_asli - p0) < 0.000001:
    print("Orde minimal = 0")
elif abs(nilai_asli - p1) < 0.000001:
    print("Orde minimal = 1")
elif abs(nilai_asli - p2) < 0.000001:
    print("Orde minimal = 2")
elif abs(nilai_asli - p3) < 0.000001:
    print("Orde minimal = 3")
elif abs(nilai_asli - p4) < 0.000001:
    print("Orde minimal = 4")
else:
    print("Galat belum kurang dari 10^-6")