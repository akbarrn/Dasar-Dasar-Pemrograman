# bilangan = int(input("Masukkan Sebuah Bilangan Bulat : "))

# if bilangan == 1 or 3 or 5 or 7 or 9 :
#     print("ganjil")
    
# else:
#     print("genap")
    
    
    #Nomor 1
# bilangan = int(input("Masukkan Bilangan Bulat: "))

# if bilangan % 2 == 0:
#     print("Bilangan Genap")
    
# else:
#     print("Bilangan Ganjil")
    
    
    #Nomor 2
# nilai = int(input("Masukkann Nilai: "))

# if nilai >= 75 :
#     print("Lulus")
    
# else:
#     print("Gagal")
    

#Nomor 3
# usia = int(input("Masukkan Usia: "))

# if usia >= 18 :
#     print("Dewasa")
    
# elif usia >= 13 and usia <= 17:
#     print("Remaja")

# else :
#     print("Anak-Anak")
    
    
#Nomor 4
# keanggotaan = input("Masukkan Status Keanggotaaan: ")

# if keanggotaan == "gold" or keanggotaan == "silver":
#     print("Selamat! Anda Mendapatkan Diskon")
    
# else:
#     print("Maaf, Anda Kurang Beruntung")
    
    #nomer 5
# jumlah = int(input("Jumlah Pembelian: "))
# total = jumlah * 0.9 if jumlah > 100 else jumlah
# print(f"Total Yang dibayar: {total}")
    
    
    
    
usia = int(input("Masukkan Usia: "))


if usia <= 5 and usia == 1:
    print("Balita")
    
elif usia <= 0:
    print("Umur Tidak Valid")
    
elif usia >= 5 and usia <= 12:
    print("Anak-Anak")
    
elif usia >= 13 and usia <= 17:
    print("Remaja")
    
elif usia >= 18 and usia <= 59:
    print("Dewasa")
    
else:
    print("Lansia")