# # kalimat = "Ini adalah sebuah kalimat"
# # kata = kalimat.split()
# # print(kata)

# inventory = ["pedang", "perisai", "roti"]
# jalan = input("pilih")
# # jalan = input("Pilih: ").split()
# match jalan:
#     case "ambil obor":
#         inventory.append("obor")
#         print("Kamu mengambil obor.")
#     case "buang roti":
#         inventory.remove("roti")
#         print("Kamu membuang roti")



inventory = ["pedang", "perisai", "roti"]
perintah = input("Perintah: ").split()

match perintah:
    case ["ambil", barang]:
        inventory.append(barang)
        print(f"Kamu mengambil {barang}.")
    case ["buang", barang]:
        if barang in inventory:
            inventory.remove(barang)
            print(f"Kamu membuang {barang}.")
        else:
            print(f"Tidak ada {barang} di inventory.")
    case ["lihat"]:
        print(f"Inventory kamu: {inventory}")
    case _:
        print("Perintah tidak dikenali.")
print(f"Inventory akhir: {inventory}")



# abdul = "Abdul lagi belajar python"
# kalimat = abdul

# print(kalimat)
