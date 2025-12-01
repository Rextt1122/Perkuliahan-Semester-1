try:
    usia = int(input("masukan usia anda :"))

    if (usia >= 17):
        kerja = input("apakah anda sudah bekerja atau masih kuliah? (kerja/kuliah) :")
        if (kerja == "kerja"):
            print("Anda sudah memiliki penghasilan")
        elif kerja == "kuliah":
            print("semangat menjalani kuliah")
        else:
            print("yang anda masukan salah")
    elif (4 < usia < 17):
        print("Anda adalah seorang siswa")
    else:
        print("Anda adalah balita")

except:
    print("Yang anda masukan bukan angka")