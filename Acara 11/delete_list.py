listHari = ['hari', 'senin', 'selasa', 'maret', 'rabu', 'kamis', 'juni']
print(listHari)

print('menghapus maret dari list :')
listHari.remove('maret')
print(listHari)

print('menghapus indeks ke 0 yaitu hari :')
del listHari[0]
print(listHari)

print('menghapus indeks ke 0 yaitu juni menggunakan pop :')
listHari.pop(0)
print(listHari)

print('menghapus indeks terakhir (kamis) menggunakan pop :')
listHari.pop()
print(listHari)

print('mencetak nilai yang dihapus pop pada indeks ke 0 yaitu senin :')
print(listHari.pop(0))