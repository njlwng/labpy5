# LAPORAN PRAKTIKUM 5
Nama : Najla Wening Khairunnisa
Nim : 312510225
Kelas : TI.25.A2
Pertemuan : 10

# Program Input Nilai Mahasiswa (Dictionary)
Program Input Nilai Mahasiswa
Program ini dibuat untuk menampilkan dan mengelola daftar nilai mahasiswa menggunakan Dictionary pada bahasa pemrograman Python.
Program memiliki fitur untuk menambah, mengubah, menghapus, menampilkan, dan mencari data nilai mahasiswa.

# Fitur Program
## 1. Tambah Data Mahasiswa
Menginput nama, nilai tugas, UTS, dan UAS.
Nilai akhir dihitung dengan rumus:
```
nilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)
```
## 2. Ubah Data Mahasiswa
Mengubah data mahasiswa yang sudah ada pada dictionary.

## 3. Hapus Data Mahasiswa
Menghapus data berdasarkan nama mahasiswa.

## 4. Tampilkan Semua Data
Menampilkan seluruh daftar mahasiswa beserta nilai lengkapnya.

## 5. Cari Data Mahasiswa
Menampilkan detail nilai satu mahasiswa berdasarkan nama.

# 📌 Struktur Data yang Digunakan
Program menggunakan Dictionary dengan format:
```python
data_mahasiswa = {
    "Nama": {
        "tugas": nilai,
        "uts": nilai,
        "uas": nilai,
        "akhir": nilai
    }
}
```
Contoh data:
```python
{
    "Najla Wening Khairunnisa": {"tugas": 90, "uts": 90, "uas": 90, "akhir": 90}
}
```
# 🧮 Perhitungan Nilai Akhir
Nilai akhir diperoleh dari 3 komponen:
Tugas = 30%
UTS = 35%
UAS = 35%

# Rumus
```
Akhir = (Tugas × 0.30) + (UTS × 0.35) + (UAS × 0.35)
```
# 📂 Flowchart Program
Berikut flowchart sederhana program input nilai mahasiswa:
```python
           +-----------------------+
           |     Mulai Program     |
           +-----------+-----------+
                       |
                       v
            +----------+----------+
            |  Tampilkan Menu     |
            +----------+----------+
                       |
                       v
          +------------+-------------+
          | Pengguna Memilih Menu?   |
          +---+-----+------+---------+
              |     |      |  
   +----------+     |      +--------------------+
   |                |                           |
   v                v                           v
+-----+     +--------------+          +-----------------+
|Tambah|    |   Ubah Data  |          |  Hapus Data     |
| Data|     +--------------+          +-----------------+
+-----+             |                         |
      \             |                         |
       \            v                         v
        \    +--------------+        +--------------------+
         \   | Tampilkan    |        |     Cari Data      |
          \  | Semua Data   |        +--------------------+
           \ +--------------+
            \
             \
              v
       +------+------+
       | Keluar?     |
       +------+------+
              |
              v
       +------+------+
       |   Selesai    |
       +-------------+
```
# Contoh Output Program
=== MENU PROGRAM NILAI MAHASISWA ===
1. Tambah Data
2. Ubah Data
3. Hapus Data
4. Tampilkan Data
5. Cari Data
0. Keluar
Pilih menu: 1

Nama: Najla Wening Khairunnisa
Nilai Tugas: 90
Nilai UTS: 90
Nilai UAS: 90
Data berhasil ditambahkan!

# 📝 Kode Program Lengkap
```
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
```
# Kesimpulan Latihan 1

Pada latihan ini dipelajari cara menggunakan Dictionary di Python untuk menyimpan dan mengelola data kontak dengan format key-value, di mana nama menjadi key dan nomor telepon menjadi value.
- Melalui latihan ini, dapat dipahami beberapa operasi dasar dictionary, yaitu:

- Membuat dictionary berisi pasangan nama dan nomor telepon.

- Mengakses data menggunakan key, misalnya menampilkan nomor telepon berdasarkan nama.

- Menambah data baru dengan menambahkan pasangan key-value baru pada dictionary.

- Mengubah value dari key yang sudah ada (update data).

- Menampilkan seluruh key (daftar nama).

- Menampilkan seluruh value (daftar nomor telepon).

- Menampilkan seluruh isi dictionary menggunakan .items().

- Menghapus data menggunakan del.

Dari latihan ini, dapat disimpulkan bahwa dictionary sangat cocok digunakan untuk menyimpan data yang memiliki pasangan atribut, seperti nama dan nomor telepon. Selain itu, dictionary memudahkan proses pencarian, perubahan, dan penghapusan data melalui key.

# Kesimpulan Tugas Praktikum

Pada tugas praktikum ini, dibuat sebuah program Python yang mengelola data nilai mahasiswa menggunakan Dictionary sebagai struktur data utama. Program memiliki fitur untuk menambah, mengubah, menghapus, mencari, dan menampilkan data mahasiswa.

Dari penyelesaian tugas ini dapat disimpulkan bahwa:

- Dictionary sangat efektif untuk menyimpan data yang memiliki banyak atribut, seperti nilai tugas, UTS, UAS, dan nilai akhir mahasiswa.
Struktur data berbentuk key-value memudahkan akses dan pengelolaan data berdasarkan nama mahasiswa.

- Program berhasil mengimplementasikan menu interaktif yang memungkinkan pengguna melakukan berbagai operasi data, sehingga lebih mudah digunakan dan fleksibel untuk pengolahan data.

- Perhitungan nilai akhir yang berasal dari 3 komponen (tugas 30%, UTS 35%, UAS 35%) dapat dilakukan dengan sederhana menggunakan operasi matematika pada Python.

- Pengelolaan data (tambah, ubah, hapus, cari) dapat dilakukan dengan cepat karena dictionary bekerja dengan akses key yang bersifat langsung (direct access).

- Melalui praktikum ini, dipahami bagaimana cara:

   -- membuat dictionary bersarang (nested dictionary),

   -- menambahkan data ke dictionary,

   -- memperbarui value,

   -- menghapus data,

   -- menampilkan seluruh data secara terstruktur.

Secara keseluruhan, praktikum ini memberikan pemahaman penting mengenai penggunaan dictionary dalam program nyata dengan konsep CRUD (Create, Read, Update, Delete). Struktur data dictionary sangat membantu dalam pengolahan data yang terorganisir dan dinamis.

