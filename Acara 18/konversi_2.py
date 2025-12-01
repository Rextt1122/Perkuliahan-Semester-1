print("==============================================")
print("WORKSHOP PEMROGRAMAN DASAR")
print("Selamat Datang di Program Konversi Suhu Sederhana")
print("==============================================")

def konversi(dari, nilai, ke):
    if dari == "C":
        c = nilai
        f = (9/5*c) + 32
        k = c + 273.15
        r = 4/5 * c
    elif dari == "F":
        f = nilai
        c = (f - 32) * 5/9
        k = c + 273.15
        r = 4/9 * (f - 32)
    elif dari == "K":
        k = nilai
        c = k - 273.15
        f = (9/5*c) + 32
        r = 4/5 * c
    elif dari == "R":
        r = nilai
        c = 5/4 * r
        f = (9/5*c) + 32
        k = c + 273.15
    else:
        return None

    if ke == "C": return c
    if ke == "F": return f
    if ke == "K": return k
    if ke == "R": return r


while True:
    print("\n1. Celcius")
    print("2. Reamur")
    print("3. Fahrenheit")
    print("4. Kelvin")

    pilih = int(input("Masukkan satuan yang akan dikonversi: "))

    if pilih == 1: satuan_asal = "C"
    elif pilih == 2: satuan_asal = "R"
    elif pilih == 3: satuan_asal = "F"
    elif pilih == 4: satuan_asal = "K"
    else:
        print("Pilihan tidak valid!")
        continue

    nilai = float(input(f"Masukkan nilai suhu {satuan_asal}: "))

    print("\nMau dikonversi ke satuan apa?")
    print("1. Celcius\n2. Reamur\n3. Fahrenheit\n4. Kelvin")
    pilih2 = int(input("Pilih = "))

    if pilih2 == 1: satuan_tuju = "C"
    elif pilih2 == 2: satuan_tuju = "R"
    elif pilih2 == 3: satuan_tuju = "F"
    elif pilih2 == 4: satuan_tuju = "K"
    else:
        print("Pilihan tidak valid!")
        continue

    hasil = konversi(satuan_asal, nilai, satuan_tuju)
    print(f"\nHasil: {nilai} {satuan_asal} = {hasil:.2f} {satuan_tuju}")

    ulang = input("\nHitung lagi? (y/n): ").lower()
    if ulang != "y":
        print("Program selesai. Makasih sudah pakai")
        break
