def hitung():
    print("===== Kalkulator Sederhana =====")
    print("Pilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("==============================")

    try:
        angka1 = float(input("Masukkan angka pertama: "))
        operator = input("Masukkan operator (+, -, *, /): ")
        angka2 = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("Error: Harap masukkan angka yang valid!")
        return

    if operator == '+':
        hasil = angka1 + angka2
        print(f"Hasil: {angka1} + {angka2} = {hasil}")
    elif operator == '-':
        hasil = angka1 - angka2
        print(f"Hasil: {angka1} - {angka2} = {hasil}")
    elif operator == '*':
        hasil = angka1 * angka2
        print(f"Hasil: {angka1} * {angka2} = {hasil}")
    elif operator == '/':
        if angka2 == 0:
            print("Error: Tidak bisa membagi dengan angka nol!")
        else:
            hasil = angka1 / angka2
            print(f"Hasil: {angka1} / {angka2} = {hasil}")
    else:
        print("Error: Operator yang Anda masukkan tidak valid.")

if __name__ == "__main__":
    while True:
        hitung()
        
        lagi = input("\nIngin melakukan perhitungan lain? (y/n): ")
        if lagi.lower() != 'y':
            print("Terima kasih telah menggunakan kalkulator!")
            break
        print("\n" + "="*30 + "\n")