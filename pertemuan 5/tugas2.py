# Nama: Akbar Nur Habibi Putra Setiawan
# NIM: 0110125123
# Kelas: SI-02


print("Program Menghitung Luas Bangun Datar")
print("1. Persegi")
print("2. lingkaran")
print("3. Segitiga")

hitung = int(input("Memilih Program (1/2/3): "))

match hitung:
    case 1:
        sisi = float(input("Masukkan panjang sisi: "))
        luas = sisi * sisi
        print(luas)
    case 2:
        r = float(input("Masukkan jari-jari lingkaran: "))
        luas = 3.14 * r * r
        print(luas)
    case 3:
        alas = float(input("Masukkan alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = 0.5 * alas * tinggi
        print(luas)
    case _:
        print("SALAH PILIH")
