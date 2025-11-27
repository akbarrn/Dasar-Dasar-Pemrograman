nama_pembeli = input("Masukkan nama pembeli: ")
nomor_hp = input("Masukkan nomor hp pembeli: ")
menu = input("Pesan menu apa? (makanan / minuman): ")

if menu == "makanan":
    jenis_makanan = input("Masukkan pesanan (nasi goreng / mie ayam / soto ayam): ")
    if jenis_makanan == "nasi goreng":
        harga = 15000
    elif jenis_makanan == "mie ayam":
        harga = 12000
    elif jenis_makanan == "soto ayam":
        harga = 13000
    else:
        print("makanan tidak tersedia.")
        harga = 0
    porsi = int(input("Berapa porsi?: "))
    total_harga = harga * porsi
    menu_dipesan = jenis_makanan

elif menu == "minuman":
    jenis_minuman = input("Masukkan pesanan (teh / kopi / jus): ")
    if jenis_minuman == "teh":
        harga = 5000
    elif jenis_minuman == "kopi":
        harga = 8000
    elif jenis_minuman == "jus":
        harga = 10000
    else:
        print("minuman tidak tersedia.")
        harga = 0
    porsi = int(input("Berapa gelas?: "))
    total_harga = harga * porsi
    menu_dipesan = jenis_minuman
    jumlah_pesanan = porsi

        

print("Nota Bill")
print(f"Nama Pembeli: {nama_pembeli}")
print(f"Nomor HP: {nomor_hp}")
print(f"Menu yang dipesan: {menu_dipesan}") 
print(f"Jumlah Pesanan: {porsi}")
print(f"Total Harga: {total_harga}")
