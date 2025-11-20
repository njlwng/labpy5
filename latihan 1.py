kontak = {
    "Ari": "081267888",
    "Dina": "087677776"
}
# Tampilkan kontak Ari
print("Kontak Ari:", kontak["Ari"])

# Tambah kontak baru
kontak["Riko"] = "087654544"
print("Kontak setelah tambah Riko:", kontak)

# Ubah kontak Dina
kontak["Dina"] = "088999776"
print("Kontak setelah update Dina:", kontak)

# Tampilkan semua Nama
print("Semua Nama:", list(kontak.keys()))

# Tampilkan semua Nomor
print("Semua Nomor:", list(kontak.values()))

# Tampilkan daftar Nama dan Nomornya
print("Daftar kontak:")
for nama, nomor in kontak.items():
    print(nama, ":", nomor)

# Hapus kontak Dina
del kontak["Dina"]
print("Setelah hapus Dina:", kontak)
