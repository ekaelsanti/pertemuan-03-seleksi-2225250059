# Pertemuan 03 Seleksi Python

 **Nama:** Eka Elsanti
 **NIM:** 2225250059
 **Kelas:** 3A

## Tujuan
Menulis program seleksi if, if-else, kondisi majemuk, dan nested if dalam bahasa pemrograman Python.

## Cara Menjalankan
```bash
python3 tugas/analisis_persamaan_kuadrat.py

```

## Algoritma Tugas

1. Menerima masukan nilai koefisien a, b, dan c sebagai tipe bilangan rasional (float).
2. Memeriksa apakah nilai a sama dengan 0. Jika ya, tampilkan pesan bahwa input bukan persamaan kuadrat.
3. Jika a tidak sama dengan 0, hitung nilai diskriminan dengan rumus D = b^2 - 4ac.
4. Menggunakan struktur nested if untuk mengevaluasi nilai diskriminan (D):
* Jika D > 0, hitung dua akar real berbeda (x1 dan x2) lalu tampilkan.
* Jika D = 0, hitung satu akar real kembar (x) lalu tampilkan.
* Jika D < 0, tampilkan pesan bahwa tidak ada akar real.



## Hasil Pengujian

| Input (a, b, c) | Hasil yang Diharapkan | Hasil Aktual | Status |
| --- | --- | --- | --- |
| a=1, b=-5, c=6 | Dua akar real: x1 = 3.00, x2 = 2.00 | Dua akar real: x1 = 3.00, x2 = 2.00 | Sesuai |
| a=1, b=2, c=1 | Akar real kembar: x = -1.00 | Akar real kembar: x = -1.00 | Sesuai |
| a=1, b=0, c=1 | Tidak ada akar real | Tidak ada akar real | Sesuai |
| a=0, b=2, c=3 | Bukan persamaan kuadrat | Bukan persamaan kuadrat | Sesuai |

## Refleksi

Salah satu hal penting yang dipelajari adalah penggunaan tanda kurung pada pembagi `(2 * a)`. Jika tidak diberi tanda kurung, operasi pembagian akan mendahulukan `-b / 2` baru dikali `a`, yang mengakibatkan kesalahan perhitungan akar.