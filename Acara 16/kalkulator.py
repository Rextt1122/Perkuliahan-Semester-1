def tambah (x, y):
    return x +  y
def kurang (x, y):
    return x - y
def kali (x, y):
    return x * y
def bagi (x, y):
    return x / y

print ("Pilih Operasi Kalkulator")
print ("1. penjumlahan")
print ("2. pengurangan")
print ("3. perkalian")
print ("4. pembagian")

pilih = input ("Masukan pilihan anda (1, 2, 3, 4) : ")
bil1 = int(input("Bilangan pertama: "))
bil2 = int(input("Bilangan kedua: "))

if pilih == '1':
    print (bil1, "+",bil2, "=", tambah (bil1,bil2))
elif pilih == '2':
    print (bil1, "-",bil2, "=", kurang (bil1,bil2))
elif pilih == '3':
    print (bil1, "*",bil2, "=", kali (bil1,bil2))
elif pilih == '4':
    print (bil1, "/",bil2, "=", bagi (bil1,bil2))
else:
    print ("Salah")