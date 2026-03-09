#data login
username = "admin"
password = "123"


data_siswa = []

#fungsui login

def login():
    while True:
        print("=== LOGIN SISTEM NILAI SISWA ===")
        
        user = input("Username : ")
        pw = input("Password : ")
        
        if user == username and pw == password:
            print("Login berhasil!\n")
            menu()
            break
        else:
            print("Login gagal! Coba lagi.\n")

#tambah data siswa
def tambah_siswa():
    nama = input("Nama siswa : ")
    kelas = input("kelas : ")
    try:
        nilai = int(input("Nilai : "))
    except ValueError:
        print("Nilai harus berupa angka!")
        return
    
    siswa = {
        "nama": nama,
        "kelas": kelas,
        "nilai": nilai
    }
    
    data_siswa.append(siswa)
    print("Data berhasil ditambahkan!")

#lihat data siswa
def lihat_siswa():
    if len(data_siswa) == 0:
        print("Belum ada data siswa")
    else:
        print("\n=== DATA NILAI SISWA ===")
        for i, siswa in enumerate(data_siswa):
            print(i+1, siswa["nama"], "-", siswa["kelas"], "-", siswa["nilai"])

#edit data siswa
def edit_siswa():
    lihat_siswa()
    
    try:
        nomor = int(input("Pilih nomor yang ingin diedit: "))
    except ValueError:
        print("Nomor harus berupa angka!")
        return
    
    if 1 <= nomor <= len(data_siswa):
        try:
            nilai_baru = int(input("Masukkan nilai baru: "))
            data_siswa[nomor-1]["nilai"] = nilai_baru
            print("Nilai berhasil diubah!")
        except ValueError:
            print("Nilai harus berupa angka!")
    else:
        print("Nomor tidak ada")

#hapus data siswa
def hapus_siswa():
    lihat_siswa()
    
    try:
        nomor = int(input("Pilih nomor yang ingin dihapus: "))
    except ValueError:
        print("Nomor harus berupa angka!")
        return
    
    if 1 <= nomor <= len(data_siswa):
        data_siswa.pop(nomor-1)
        print("Data berhasil dihapus!")
    else:
        print("Nomor tidak ditemukan")

#menu utama
def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Tambah Data Siswa")
        print("2. Lihat Data Siswa")
        print("3. Edit Nilai")
        print("4. Hapus Data")
        print("5. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            while True:
                try:
                    jumlah = int(input("Berapa data siswa yang ingin ditambahkan? "))
                    break
                except ValueError:
                    print("Jumlah harus berupa angka! Coba lagi.")
            for _ in range(jumlah):
                tambah_siswa()
        elif pilihan == "2":
            lihat_siswa()
        elif pilihan == "3":
            edit_siswa()
        elif pilihan == "4":
            hapus_siswa()
        elif pilihan == "5":
            print("Program selesai")
            break
        else:
            print("Menu tidak tersedia")

#jalankan program
login()