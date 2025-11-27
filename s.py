# Program Kalkulator Sederhana

# Input
angka1 = float(input("Masukkan angka 1 : "))
angka2 = float(input("Masukkan angka 2 : "))
operator = input("Pilih operator (+, -, *, /, **) : ")

# Proses dan Output
print("Angka pertama :", angka1)
print("Angka kedua   :", angka2)

if operator == "+":
    hasil = angka1 + angka2
    print("Pilihan Operator : tambah")
    print(f"Hasil operator {angka1} + {angka2} = {hasil}")

elif operator == "-":
    hasil = angka1 - angka2
    print("Pilihan Operator : kurang")
    print(f"Hasil operator {angka1} - {angka2} = {hasil}")

elif operator == "*":
    hasil = angka1 * angka2
    print("Pilihan Operator : kali")
    print(f"Hasil operator {angka1} x {angka2} = {hasil}")

elif operator == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
        print("Pilihan Operator : bagi")
        print(f"Hasil operator {angka1} / {angka2} = {hasil}")
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan!")

elif operator == "**":
    hasil = angka1 ** angka2
    print("Pilihan Operator : pangkat")
    print(f"Hasil operator {angka1} ** {angka2} = {hasil}")

else:
    print("Operator tidak dikenali!")
