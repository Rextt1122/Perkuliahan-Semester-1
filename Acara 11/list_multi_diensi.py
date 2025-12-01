list_minuman = [
    ["Kopi", "Susu", "Teh"],
    ["Jus Apel", "Jus Melon", "Jus Jeruk"],
    ["Es Anggur", "Es Campur", "Es Teler"]
]

print (list_minuman)
print('\n')

print ("Menampilkan salah satu menu dengan menunjuk nomor indeks :")
print (list_minuman[0][0])
print (list_minuman[1][2])
print('\n')

print ("Menampilkan isi list :")
for menu in list_minuman:
    print (menu)

print ('\n')
print ("Menampilkan isi list di dalam list :")
for menu in list_minuman:
    for minuman in menu:
        print(minuman)