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
print ('Alamat: ', mahasiswa.get('alamat'))
mahasiswa ['alamat'] = 'Lumajang'

print ('Mahasiswa {} beralamat di {}'.format(
    mahasiswa.get ('nama'),
    mahasiswa.get ('alamat')
))
