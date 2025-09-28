# Mini Project CRUD - Sistem Penyewaan Mobil dengan Dictionary, Looping, Functions, Error Handling, dan Sistem Login

daftar_mobil = {
    1: {'merk': 'Toyota', 'model': 'Avanza', 'tahun': 2022, 'harga': 350000, 'status': 'Tersedia'},
    2: {'merk': 'Honda', 'model': 'Civic', 'tahun': 2023, 'harga': 500000, 'status': 'Tersedia'},
    3: {'merk': 'Suzuki', 'model': 'Ertiga', 'tahun': 2021, 'harga': 300000, 'status': 'Tersedia'}
}

KAPASITAS_MAKSIMAL = 10

def hitung_jumlah_mobil():
    jumlah = 0
    for kunci in daftar_mobil:
        jumlah = jumlah + 1
    return jumlah

def dapatkan_id_selanjutnya():
    if not daftar_mobil:
        return 1
    id_maks = 0
    for kunci in daftar_mobil:
        if kunci > id_maks:
            id_maks = kunci
    return id_maks + 1

def validasi_status(status):
    return status == 'Tersedia' or status == 'Disewa'

def sistem_login():
    print("\n--- Sistem Login ---")
    print("Role tersedia:")
    print("1. Manager (Username: manager, Password: admin)")
    print("2. Karyawan (Username: karyawan, Password: user)")
    pilihan_role = input("Pilih role (1-2): ")
    if pilihan_role == '1':
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if username == 'manager' and password == 'admin':
            return 'manager'
        else:
            print("Login gagal. Gunakan role Karyawan.")
            return 'karyawan'
    elif pilihan_role == '2':
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if username == 'karyawan' and password == 'user':
            return 'karyawan'
        else:
            print("Login gagal.")
            return None
    else:
        print("Pilihan tidak valid.")
        return None

def tampilkan_menu(role):
    print("\n--- Sistem Penyewaan Mobil ---")
    if role == 'manager':
        print("1. Tambah Mobil")
        print("2. Lihat Daftar Mobil")
        print("3. Perbarui Data Mobil")
        print("4. Hapus Mobil")
        print("5. Keluar")
    else:
        print("1. Lihat Daftar Mobil")
        print("2. Perbarui Status Mobil")
        print("3. Keluar")

def tambah_mobil():
    if hitung_jumlah_mobil() >= KAPASITAS_MAKSIMAL:
        print("Kapasitas penuh (maksimal 10 data).")
        return
    print("\n--- Tambah Mobil Baru ---")
    try:
        merk = input("Masukkan merk mobil: ")
        if merk == '':
            raise ValueError("Merk kosong.")
        model = input("Masukkan model mobil: ")
        if model == '':
            raise ValueError("Model kosong.")
        tahun_input = input("Masukkan tahun mobil: ")
        tahun = int(tahun_input)
        if tahun < 1900 or tahun > 2025:
            raise ValueError("Tahun tidak valid.")
        harga_input = input("Masukkan harga sewa per hari: ")
        harga = int(harga_input)
        if harga <= 0:
            raise ValueError("Harga tidak valid.")
        status = 'Tersedia'
        id_baru = dapatkan_id_selanjutnya()
        daftar_mobil[id_baru] = {'merk': merk, 'model': model, 'tahun': tahun, 'harga': harga, 'status': status}
        print("Mobil ditambahkan!")
        print("Data baru:", daftar_mobil[id_baru])
    except ValueError as e:
        print("Error:", e)
    except:
        print("Kesalahan menambah data.")

def lihat_mobil():
    print("\n--- Daftar Mobil ---")
    if not daftar_mobil:
        print("Tidak ada data.")
        return
    print("No. | Merk | Model | Tahun | Harga/hari | Status")
    print("-" * 50)
    urutan = 1
    for id_mobil in daftar_mobil:
        detail = daftar_mobil[id_mobil]
        print(f"{urutan}. | {detail['merk']} | {detail['model']} | {detail['tahun']} | Rp {detail['harga']:,} | {detail['status']}")
        urutan = urutan + 1

def perbarui_mobil_lengkap():
    if not daftar_mobil:
        print("Tidak ada data.")
        return
    lihat_mobil()
    try:
        jumlah = hitung_jumlah_mobil()
        nomor_input = input(f"Masukkan nomor (1-{jumlah}): ")
        nomor = int(nomor_input)
        if nomor < 1 or nomor > jumlah:
            raise ValueError("Nomor tidak valid.")
        kunci_list = list(daftar_mobil.keys())
        id_aktual = kunci_list[nomor - 1]
        data_lama = daftar_mobil[id_aktual]
        print("Data lama:", data_lama)
        merk_baru = input(f"Merk baru ({data_lama['merk']}): ") or data_lama['merk']
        model_baru = input(f"Model baru ({data_lama['model']}): ") or data_lama['model']
        tahun_input = input(f"Tahun baru ({data_lama['tahun']}): ")
        tahun_baru = int(tahun_input) if tahun_input else data_lama['tahun']
        if tahun_baru < 1900 or tahun_baru > 2025:
            raise ValueError("Tahun tidak valid.")
        harga_input = input(f"Harga baru (Rp {data_lama['harga']}): ")
        harga_baru = int(harga_input) if harga_input else data_lama['harga']
        if harga_baru <= 0:
            raise ValueError("Harga tidak valid.")
        status_input = input(f"Status baru ({data_lama['status']}): ")
        status_baru = status_input if validasi_status(status_input) else data_lama['status']
        daftar_mobil[id_aktual] = {'merk': merk_baru, 'model': model_baru, 'tahun': tahun_baru, 'harga': harga_baru, 'status': status_baru}
        print("Data diperbarui!")
        print("Data baru:", daftar_mobil[id_aktual])
    except ValueError as e:
        print("Error:", e)
    except:
        print("Kesalahan perbarui data.")

def perbarui_status_saja():
    if not daftar_mobil:
        print("Tidak ada data.")
        return
    lihat_mobil()
    try:
        jumlah = hitung_jumlah_mobil()
        nomor_input = input(f"Masukkan nomor (1-{jumlah}): ")
        nomor = int(nomor_input)
        if nomor < 1 or nomor > jumlah:
            raise ValueError("Nomor tidak valid.")
        kunci_list = list(daftar_mobil.keys())
        id_aktual = kunci_list[nomor - 1]
        data_lama = daftar_mobil[id_aktual]
        print("Status lama:", data_lama['status'])
        status_input = input("Status baru (Tersedia/Disewa): ")
        if not validasi_status(status_input):
            print("Status tidak valid.")
            return
        daftar_mobil[id_aktual]['status'] = status_input
        print("Status diperbarui!")
        print("Status baru:", status_input)
    except ValueError as e:
        print("Error:", e)
    except:
        print("Kesalahan perbarui status.")

def hapus_mobil():
    if not daftar_mobil:
        print("Tidak ada data.")
        return
    lihat_mobil()
    try:
        jumlah = hitung_jumlah_mobil()
        nomor_input = input(f"Masukkan nomor (1-{jumlah}): ")
        nomor = int(nomor_input)
        if nomor < 1 or nomor > jumlah:
            raise ValueError("Nomor tidak valid.")
        kunci_list = list(daftar_mobil.keys())
        id_aktual = kunci_list[nomor - 1]
        del daftar_mobil[id_aktual]
        print("Mobil dihapus!")
        lihat_mobil()
    except ValueError as e:
        print("Error:", e)
    except:
        print("Kesalahan hapus data.")

def program_utama():
    role = sistem_login()
    if role is None:
        print("Login gagal, Silahlan Jalankan Ulang Program")
        return
    if role == 'manager':
        print("\nSelamat datang, Manager!")
    else:
        print("\nSelamat datang, Karyawan!")
    while True:
        tampilkan_menu(role)
        pilihan = input("Masukkan pilihan: ")
        if role == 'manager':
            if pilihan == '1':
                tambah_mobil()
            elif pilihan == '2':
                lihat_mobil()
            elif pilihan == '3':
                perbarui_mobil_lengkap()
            elif pilihan == '4':
                hapus_mobil()
            elif pilihan == '5':
                print("Terima kasih!")
                break
            else:
                print("Pilihan tidak valid.")
        else:
            if pilihan == '1':
                lihat_mobil()
            elif pilihan == '2':
                perbarui_status_saja()
            elif pilihan == '3':
                print("Terima kasih!")
                break
            else:
                print("Pilihan tidak valid.")
        input("\nTekan Enter untuk lanjut...")

program_utama()
