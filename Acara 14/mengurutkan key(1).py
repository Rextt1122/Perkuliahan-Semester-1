mahasiswa ={
    "nama" : "Biyann",
    "usia" : 17,
    "kelamin" : "Laki-laki",
    "menikah" : False,
    "hobi" : ["Berenang", "Bersepeda"],
    "kuliah" : {
        "jurusan" : "Teknologi Informasi",
        "prodi" : "D3 Teknik Komputer"
    }
}

for key in sorted(mahasiswa) :
    print ("%s: %s" % (key, mahasiswa [key]))