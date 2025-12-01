# Membuat set
buah = {"apel", "jeruk", "mangga", "pisang"}

# Menampilkan isinya satu per satu
for item in buah:
    print(item)



# Nested set menggunakan frozenset
nested = {
    frozenset({"apel", "jeruk"}),
    frozenset({"mangga", "pisang"})
}

# Menampilkan isinya satu per satu
for subset in nested:
    print(subset)
    for item in subset:
        print(" -", item)

