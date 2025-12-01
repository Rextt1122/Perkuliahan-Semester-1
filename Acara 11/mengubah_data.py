listKata = ["mangga", "jambu", "apel", "anggu"]
print(listKata)

print("Sesudah indeks ke 1 diubah :")
listKata[1] = "rambutan"
print(listKata)

print('List juga bisa ditambahkan :')
print(listKata+["delima", "melon", "pear"])

print('List juga bisa ditambahkan kemudian disimpan :')
listKata=listKata+["delima", "melon", "pear"]
print(listKata)

print('List juga bisa dikalikan :')
print(listKata*2)

print("apel" in listKata)
print("Salak" in listKata)
if "melon" in listKata:
    print("Ada melon di dalam listKata")