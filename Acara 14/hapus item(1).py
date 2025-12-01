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
del mahasiswa ['nama']
print ('Nama Mahasiswa:', mahasiswa.get('nama'))

mahasiswa.pop ('usia')
print ('Usia mahasiswa', mahasiswa.get('usia'))

gender = mahasiswa.pop ('kelamin')
print ('Jenis kelamin mahasiswa:', gender)