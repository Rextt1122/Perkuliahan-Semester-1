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
print ('Nama awal:', mahasiswa.get('nama'))
mahasiswa['nama'] = 'Kaoruko waguri'
print ('Nama setelah diubah', mahasiswa.get('nama'))