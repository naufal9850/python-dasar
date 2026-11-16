#open()
# Membaca isi file
file = open("data.txt", "r")  # "r" = read
print(file.read())
file.close()


#baca file baris per baris
file = open("data.txt", "r")
for baris in file:
    print(baris.strip())  # strip() untuk hapus newline
file.close()

# Menulis ke file
# Menulis file baru atau menimpa file lama
file = open("data.txt", "w")
file.write("Halo, ini data baru!\n")
file.write("Baris kedua...\n")
file.close()


#mnambahkan data ke file
# Menambah data di akhir file
file = open("data.txt", "a")
file.write("Baris tambahan...\n")
file.close()

#menggunakan with untuk best pratice
with open("data.txt", "r") as file:
    isi = file.read()
    print(isi)

#contoh legkap
# Menulis file
with open("contoh.txt", "w") as file:
    file.write("Belajar Python itu menyenangkan!\n")

# Menambah data
with open("contoh.txt", "a") as file:
    file.write("Tambahan baris kedua.\n")

# Membaca file
with open("contoh.txt", "r") as file:
    for baris in file:
        print(baris.strip())
