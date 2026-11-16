# Membuat dictionary sederhana
mahasiswa = {
    "nama": "yantii",
    "umur": 20,
    "jurusan": "Informatika"
}

print(mahasiswa)

#mengakses data

print(mahasiswa["nama"])    # Budi
print(mahasiswa.get("umur")) # 20

#menambah dan mengubah data 

mahasiswa["angkatan"] = 2025 # Menambah data baru
mahasiswa["umur"] = 21         # Mengubah value umur

print(mahasiswa)

mahasiswa.pop("jurusan")   # Menghapus dengan key
del mahasiswa["nama"]      # Menghapus dengan del

print(mahasiswa)


#menghaus data
mahasiswa.pop("jurusan")   # Menghapus dengan key
del mahasiswa["nama"]      # Menghapus dengan del

print(mahasiswa)

#iterasi dictionary
for key, value in mahasiswa.items():
    print(key, ":", value)

#nasted dictionary
kampus = {
    "mahasiswa1": {"nama": "Budi", "umur": 21},
    "mahasiswa2": {"nama": "Siti", "umur": 22}
}

print(kampus["mahasiswa1"]["nama"])  # Budi

