#Nama: Akbar Nur Habibi Putra Setiawan
#NIM: 0110125123
#Kelas: SI-02
#Tugas Praktikum Asdos

usia = int(input("Masukkan Usia: "))

if usia <= 0:
    print("Umur Tidak Valid")

elif usia >= 1 and usia <= 5:
    print("Balita")

elif usia >= 6 and usia <= 12:
    print("Anak-Anak")

elif usia >= 13 and usia <= 17:
    print("Remaja")

elif usia >= 18 and usia <= 59:
    print("Dewasa")

else:
    print("Lansia")
