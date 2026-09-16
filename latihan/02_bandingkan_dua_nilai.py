# Latihan 2: Membandingkan Dua Bilangan dengan Nested If
a = float(input("Bilangan pertama: "))
b = float(input("Bilangan kedua: "))

if a >= b:
    if a == b:
        print("Kedua bilangan sama.")
    else:
        print("Bilangan pertama lebih besar.")
else:
    print("Bilangan pertama lebih kecil.")