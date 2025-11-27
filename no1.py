
nama_kendaraan = input("Masukkan nama kendaraan: (mobil/motor): ")
jenis_bensin = input("Masukkan jenis bensin (pertalite/pertamax/pertamax turbo): ")
kota_tujuan = input("Jakarta/bekasi/tangerang/bogor/depok: ")

if kota_tujuan == "jakarta":
    
    jarak_kota = 20
elif kota_tujuan == "bekasi":
    jarak_kota = 35.7
elif kota_tujuan == "tangerang":
    jarak_kota = 99
elif kota_tujuan == "bogor":
    jarak_kota = 120.6
elif kota_tujuan == "depok":
    jarak_kota = 5

if jenis_bensin == "pertalite":
    liter = 10000
    jarak_bensin = 12
elif jenis_bensin == "pertamax":
    liter = 14000
    jarak_bensin = 13
elif jenis_bensin == "pertamax turbo":
    liter = 17000
    jarak_bensin = 13.5

  

pemakaian_bensin = round(jarak_kota / jarak_bensin)
total_harga_bensin = round(pemakaian_bensin * liter)

print(f"Nama Kendaraan: {nama_kendaraan}")
print(f"Jenis Bensin: {jenis_bensin}")
print(f"Kota Tujuan: {kota_tujuan}")
print(f"Pemakaian Bensin: {pemakaian_bensin}")
print(f"Total Harga Bensin: {total_harga_bensin}")
