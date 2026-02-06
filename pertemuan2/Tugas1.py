#==================================================
#TUGAS1
#Sistem stok barang kantin
#==================================================

#konstanta nama file 
NAMA_FILE = "data_barang.txt"

#Fungsi untuk membaca data dari file ke dalam dictionary
def baca_stok(nama_file):
    """
    membaca daat stok dari file teks
    format per baris: KodeBarang,Namabarang,Stok
    Output: stok_dict dengan key = KodeBarang
    """
    stok_dict={}
    try:
        #gunakan 'with open' agar file otomatis tertutup
        with open(nama_file,"r",encoding="utf-8") as f:
            for baris in f:
                baris=baris.strip()        #menghilangkan karakter \n
                if not baris:
                    continue

                #memecah baris menjadi kolom berdasarkan koma
                parts = baris.split(",")
                if len(parts) == 3:
                    kode, nama, stok = parts
                    #menyimpan ke dictionary dengan konversi stok ke integer
                    stok_dict[kode] = {"nama": nama,"stok": int(stok)}
    except FileNotFoundError:
        #jika file belum ada, program berjalan dengan data kosong
        pass
    return stok_dict

#Fungsi untuk menyimpan data dar dictionary kembali ke file
def simpan_stok(nama_file, stok_dict):
    """
    Menulis ulang seluruh data dari dictionary ke file teks
    """
    with open(nama_file, "w", encoding="utf-8") as f:
        for kode in sorted(stok_dict.keys()):
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            f.write(f"{kode}, {nama}, {stok}\n")

#Fungsi untuk menampilkan seluruh data barang
def tampilkan_semua(stok_dict):
    """
    menampilkan semua barang dalam format tabel
    """
    if not stok_dict:
        print("\nStok barang kosong.")
        return
    
    print("\n===DAFTAR STOK BARANG===")
    #Menggunakan f-string formatting agar kolom sejajar
    print(f"{'Kode':<10} | {'Nama Barang':<15} | {'Stok':>5}")
    print("-" * 35)
    for kode in sorted(stok_dict.keys()):
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print(f"{kode:<10} | {nama:<15} | {stok:>5}")


#Fungsi untuk mencari barang berdasarkan kode
def cari_barang(stok_dict):
    """
    Mencari data barang berdasarkan key 
    """
    kode = input("Masukkan kode barnag yang dicari: ").strip()
    if kode in stok_dict:
        print(f"\nBarang Ditemukan: {kode} - {item['nama']} (Stok: {item['stok']})")
    else:
        print("\nBarang Tidak Ditemukan.")


#Fungsi untuk menambah barang baru
def tambah_barang(stok_dict):
    """
    Menambahkan entittas barang baru ke dalam dictionary
    """
    kode = input("Masukkan kode barang baru: ").strip()
    if kode in stok_dict:
        print("Kode sudah digunakan. Tambah barang dibatalkan.") [cite: 72]
        return
    
    nama = input("Masukkan nama barang: ").strip()
    try:
        stok_awal = int(input("Masukkan stok awal: "))
        stok_dict[kode] = {"nama": nama, "stok": stok_awal}
        print("Barang berhasil ditemukan.")
    except ValueError:
        print("Input stok harus berupa angka.")


#Fungsi untuk update(tambah/kurangi) stok barang
def update_stok(stok_dict):
    """
    Mengubah jumlah stok barang yang sudah ada
    """
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()
    if kode not in stok_dict:
        print("Kode barang tidak ditemukan.")
        return
    
    print("1. Tambah stok\n2. Kurangi stok")
    pilihan = input("Pilihan (1/2): ")

    try:
        jumlah = int(input("Masukkan jumlah: "))
        if pilihan == "1":
            stok_dict[kode]["stok"] += jumlah
        elif pilihan == "2":
            #Validasi agar stok tidak negatif
            if stok_dict[kode]["stok"] - jumlah < 0:
                print("Error: Stok tidak boleh negatif.")
            else:
                stok_dict[kode]["stok"] += jumlah
        print("Update stok berhasil.")
    except ValueError:
        print("Input jumlah harus berupa angka.")


#Program utama (Menu Interaktif)
def main():
    #Load data dari file saat program pertama kali dijalankan
    data_barang = baca_stok(NAMA_FILE)

    while True:
        print("\n===MENU STOK KANTIN===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Piihan menu: ").strip()

        if pilihan == "1":
            tampilkan_semua(data_barang)
        elif pilihan == "2":
            cari_barang(data_barang)
        elif pilihan == "3":
            tambah_barang(data_barang)
        elif pilihan == "4":
            update_stok(data_barang)
        elif pilihan == "5":
            simpan_stok(NAMA_FILE, data_barang)
            print("Data berhasil disimpan ke", NAMA_FILE)
        elif pilihan "0":
            pilihan("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
