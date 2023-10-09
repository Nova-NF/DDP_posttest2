# Menampilkan judul program
print("NOVA COFFE")

# Data penjualan kopi dalam bentuk daftar dictionary
list_kopi = [
    {"id": 1, "nama": "arabica", "harga": 30000, "stok": "100g"},
    {"id": 2, "nama": "robusta", "harga": 40000, "stok": "500g"},
    {"id": 3, "nama": "liberica", "harga": 60000, "stok": "300g"},
]

# Fungsi untuk menambahkan data penjualan (Create)
def tambah_penjualan(nama, harga, stok):
    # Menghitung ID baru dengan mengambil panjang (jumlah elemen) dari list_kopi dan menambahkan 1
    new_id = len(list_kopi) + 1
    # Membuat dictionary baru untuk data penjualan dan menambahkannya ke list_kopi
    list_kopi.append({
        "id": new_id,
        "nama": nama,
        "harga": harga,
        "stok": stok
    })
    # Menampilkan pesan sukses
    print("Data berhasil ditambahkan")

# Fungsi untuk menampilkan data penjualan (Read)
def tampilkan_kopi():
    # Memeriksa apakah list_kopi kosong
    if not list_kopi:
        # Jika kosong, mencetak pesan
        print("Data kopi kosong")
    else:
        # Jika tidak kosong, mencetak detail data penjualan
        print("Data kopi:")
        for kopi in list_kopi:
            print(
                f"ID: {kopi['id']}, Nama: {kopi['nama']}, harga: {kopi['harga']}, Stok: {kopi['stok']}")

# Fungsi untuk mengupdate data penjualan (Update)
def update_kopi(id, nama, harga, stok):
    for kopi in list_kopi:
        if kopi["id"] == id:
            # Mengganti nilai nama, harga, dan stok dengan nilai baru
            kopi["nama"] = nama
            kopi["harga"] = harga
            kopi["stok"] = stok
            # Menampilkan pesan sukses
            print("Data kopi berhasil diperbarui")
            return
    # Jika ID tidak ditemukan, mencetak pesan kesalahan
    print("Data kopi tidak ditemukan")

# Fungsi untuk menghapus data penjualan (Delete)
def hapus_kopi(id):
    for kopi in list_kopi:
        if kopi["id"] == id:
            # Menghapus data penjualan dengan ID tertentu dari list_kopi
            list_kopi.remove(kopi)
            # Menampilkan pesan sukses
            print("Data kopi berhasil dihapus")
            return
    # Jika ID tidak ditemukan, mencetak pesan kesalahan
    print("Data kopi tidak ditemukan")

# Daftar username dan password untuk autentikasi
list_username = [{"username": "nova", "password": "123123"}]

# Fungsi untuk melakukan autentikasi (login)
def login(username, password):
    for user in list_username:
        if user["username"] == username and user["password"] == password:
            # Mengembalikan True jika autentikasi berhasil
            return True
        else:
            # Mencetak pesan gagal jika autentikasi gagal
            print("login gagal")

# Menampilkan pilihan peran (admin atau pembeli)
print("Pilihan Role")
print("1. admin")
print("2. pembeli")

# Meminta input peran dari pengguna (admin atau pembeli)
pilihan = int(input("Masukkan pilihan (1-2): "))

# Blok kode untuk peran admin
if pilihan == 1:
    print("selamat datang admin")

    # Meminta input username dan password dari admin
    username = input("masukan username:")
    password = input("masukan password:")

    # Melakukan autentikasi admin
    if login(username, password):
        print("login berhasil")
        while True:
            # Menampilkan menu admin
            print("\nPilihan Menu:")
            print("1. Tambah Data Penjualan")
            print("2. Tampilkan Data Penjualan")
            print("3. Update Data Penjualan")
            print("4. Hapus Data Penjualan")
            print("5. Keluar")

            # Meminta input menu dari admin
            pilihan = input("Masukkan pilihan: ")

            if pilihan == "1":
                # Meminta input data untuk penambahan data penjualan
                nama = input("Masukkan nama kopi: ")
                harga = int(input("Masukkan harga: "))
                stok = input("Masukkan stok: ")
                # Memanggil fungsi tambah_penjualan
                tambah_penjualan(nama, harga, stok)
            elif pilihan == "2":
                # Menampilkan data penjualan
                tampilkan_kopi()
            elif pilihan == "3":
                # Meminta input ID data penjualan yang ingin diperbarui
                id = int(input("Masukkan ID data penjualan yang ingin diperbarui: "))
                # Meminta input data baru untuk update
                nama = input("Masukkan nama kopi baru: ")
                harga = int(input("Masukkan harga baru: "))
                stok = input("Masukkan stok baru: ")
                # Memanggil fungsi update_kopi
                update_kopi(id, nama, harga, stok)
            elif pilihan == "4":
                # Meminta input ID data penjualan yang ingin dihapus
                id = int(input("Masukkan ID data penjualan yang ingin dihapus: "))
                # Memanggil fungsi hapus_kopi
                hapus_kopi(id)
            elif pilihan == "5":
                # Keluar dari peran admin
                break
            else:
                # Jika input menu tidak valid, mencetak pesan kesalahan
                print("Pilihan tidak valid")
        else:
            # Jika autentikasi admin gagal, mencetak pesan kesalahan
            print("login gagal")

# Blok kode untuk peran pembeli
if pilihan == 2:
    print("Selamat datang di NOVA COFFE!")
    print("Pilihan kopi:")
    print("1. arabica")
    print("2. robusta")
    print("3. liberica")

    # Meminta input pilihan kopi dari pembeli
    pilihan = input("Masukkan nomor pilihan Anda: ")

    if pilihan == "1":
        jenis_kopi = "arabica"
        harga_per_gram = 30000

    elif pilihan == "2":
        jenis_kopi = "robusta"
        harga_per_gram = 40000

    elif pilihan == "3":
        jenis_kopi = "liberica"
        harga_per_gram = 60000

    else:
        # Jika input pilihan tidak valid, mencetak pesan kesalahan dan keluar dari program
        print("Pilihan tidak valid.")
        exit()

    # Meminta input jumlah gram yang ingin dibeli oleh pembeli
    jumlah_gram = float(input(f"Berapa gram {jenis_kopi} yang ingin Anda beli? "))
    total_harga = jumlah_gram * harga_per_gram

    # Menampilkan informasi pembelian
    print(f"Anda telah memilih {jumlah_gram} gram {jenis_kopi}.")
    print(f"Total harga yang harus Anda bayar adalah Rp.{total_harga}.")
