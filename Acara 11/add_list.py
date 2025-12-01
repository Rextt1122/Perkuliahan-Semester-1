nomor = [1, 5, 9, 7, 5, 11]

print('menghitung jumlah item pada list :')
print(len(nomor))

print('menambah angka 13 menggunakan append:')
nomor.append(13)
print(nomor)

print('menyisipkan angka 3 pada indeks ke-1 menggunakan insert :')
indeks = 1
nomor.insert(indeks, 3)
print(nomor)

print('menambah list berisi 15, 17, 19 pada list nomor :')
nomor.extend([15, 17, 19])
print(nomor)

print('cek angka 1 di indeks keberapa? angka 2 di indeks keberapa?')
print(nomor.index(1))
print(nomor.index(2))