
jenis_kendaraan = input("Masukkan jenis kendaraan (mobil/motor): ")
bensin = ['pertalite', 'pertamax', 'pertamax turbo']
jenis_bensin = input("Masukkan jenis bensin (premium/pertalite/pertamax): ")
kota = input("Masukkan kota tujuan: ")
harga = int(('1.000'))
liter = float(("Masukkan jumlah liter bensin yang diisi: "))
total_harga = harga * liter


print(f"Jenis Kendaraan: {jenis_kendaraan}")
print(f"Jenis Bensin: {jenis_bensin}")
print(f"Kota Tujuan: {kota}")
print(f"Total Harga Bensin: Rp {total_harga}")




# inventory = ["pedang", "perisai", "roti"]
# perintah = input("Perintah: ").split()

# match perintah:
#     case ["ambil", barang]:
#         inventory.append(barang)
#         print(f"Kamu mengambil {barang}.")
#     case ["buang", barang]:
#         if barang in inventory:
#             inventory.remove(barang)
#             print(f"Kamu membuang {barang}.")
#         else:
#             print(f"Tidak ada {barang} di inventory.")
#     case ["lihat"]:
#         print(f"Inventory kamu: {inventory}")
#     case _:
#         print("Perintah tidak dikenali.")
# print(f"Inventory akhir: {inventory}")












# jkt 20km bekasi 35.7 dpk 5km tgrng 99km bogor 120.6km

# lite 10.000/liter - 12km
# max 14.000/liter - 13km
# turbo 17.000/liter - 13.5km

# pemakaian bensin = jarak kota : jarak tempuh bensin 

# total harga bensin


# kendaraan = ['mobil', 'motor']
# jenis_bensin = ['pertalite', 'pertamax', 'pertamax turbo']
# kota_tujuan = {
#     'jakarta': 20,
#     'bekasi': 35.7,
#     'tangerang': 99,
#     'bogor': 120.6
# }
# harga_bensin = {
#     'pertalite': 10000,
#     'pertamax': 14000,
#     'pertamax turbo': 17000
# }


# print(input(f"Masukkan jenis kendaraan (mobil/motor): "))
# print(input("Masukkan jenis bensin (pertalite/pertamax/pertamax turbo): "))
# print(input("Masukkan kota tujuan (jakarta/bekasi/tangerang/bogor): "))
