data_mahasiswa = {}
def tambah_data():
    nama = input("Nama: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

    data_mahasiswa[nama] = {
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "akhir": akhir
    }
    print("Data berhasil ditambahkan!\n")


def ubah_data():
    nama = input("Masukkan nama yang ingin diubah: ")
    if nama in data_mahasiswa:
        print("Isi ulang datanya:")
        tugas = float(input("Nilai Tugas: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))

        akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

        data_mahasiswa[nama] = {
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "akhir": akhir
        }
        print("Data berhasil diubah!\n")
    else:
        print("Nama tidak ditemukan!\n")

def hapus_data():
    nama = input("Masukkan nama yang ingin dihapus: ")
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print("Data berhasil dihapus!\n")
    else:
        print("Nama tidak ditemukan!\n")

def tampilkan_data():
    if not data_mahasiswa:
        print("Belum ada data.\n")
        return

    print("\nDaftar Nilai Mahasiswa")
    print("=" * 50)
    print(f"{'Nama':10} {'Tugas':7} {'UTS':7} {'UAS':7} {'Akhir':7}")
    print("=" * 50)

    for nama, nilai in data_mahasiswa.items():
        print(f"{nama:10} {nilai['tugas']:7} {nilai['uts']:7} {nilai['uas']:7} {nilai['akhir']:7.2f}")
    print()

def cari_data():
    nama = input("Masukkan nama yang dicari: ")
    if nama in data_mahasiswa:
        nilai = data_mahasiswa[nama]
        print("\nData ditemukan:")
        print("Nama :", nama)
        print("Tugas:", nilai["tugas"])
        print("UTS  :", nilai["uts"])
        print("UAS  :", nilai["uas"])
        print("Akhir:", nilai["akhir"])
        print()
    else:
        print("Data tidak ditemukan!\n")

# MENU PROGRAM
while True:
    print("=== MENU PROGRAM NILAI MAHASISWA ===")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("0. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        ubah_data()
    elif pilihan == "3":
        hapus_data()
    elif pilihan == "4":
        tampilkan_data()
    elif pilihan == "5":
        cari_data()
    elif pilihan == "0":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!\n")
