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

print ('Nama mahasiswa:', mahasiswa.get('nama'))
print ('Usia mahasiswa:', mahasiswa.get('usia'))
print ('Jurusan mahasiswa:', mahasiswa.get('kuliah').get('jurusan'))
print ('Prodi mahasiswa:', mahasiswa ['kuliah']['prodi'])