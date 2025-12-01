try:
    angka1= 9

    print(angka1 + "buah")

except ZeroDivisionError:
    print("terjadi pembagian akngka 0")
except (ValueError,TypeError):
    print ("terjadi error pada value atau type")