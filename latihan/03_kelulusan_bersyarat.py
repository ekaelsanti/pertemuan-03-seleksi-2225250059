# Latihan 3: Kelulusan Bersyarat (Nilai >= 60 dan Kehadiran >= 80%)
nilai = float(input("Nilai akhir: "))
kehadiran = float(input("Kehadiran (%): "))

if nilai >= 60 and kehadiran >= 80:
    print("Lulus")
else:
    print("Belum lulus")