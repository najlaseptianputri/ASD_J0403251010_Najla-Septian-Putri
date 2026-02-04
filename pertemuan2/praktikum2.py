#================================================
#Praktikum 2 : Konsep ADT dan file handling(STUDI KASUS)
#Latihan 1: MEMBUAT FUNGSI LOAD
#================================================

nama_file = "data_mahasiswa.txt"

#membuat fungsi membaca data mahasiswa
def baca_data_mahasiswa(nama_file):
    data_dict ={}  #inisialisasi data dictionary
    with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
        for baris in file:
            baris= baris.strip()

            parts = baris.split(",")
            if len(parts) != 3:
                continue
            nim, nama, nilai_str = parts
            nilai_int = int(nilai_str)
            data_dict[nim]  = {"nama": nama, "nilai": nilai_int}
            nim,nama,nilai=baris.split(",")
        #simpan data mahasiswa ke dictionary dengan key NIM
            data_dict[nim] = {          #key
                "nama": nama,           #values
                "nilai": int(nilai)     #values
            }
    return(data_dict)

#memanggil fungsi baca_data_mahasiswa
buka_data = baca_data_mahasiswa(nama_file)
print("Jumlah data terbaca", len(buka_data)) 

#================================================
#Praktikum 2 : Konsep ADT dan file handling(STUDI KASUS)
#Latihan 2: membuat fungsi menamilkan data
#================================================


def tampilkan_data(data_dict):
    
    if len(data_dict) == 0:
        print ("Data kosong")
        return
    #membuat header tabel
    print("\n====Daftar Mahasiswa====")
    print(f"{'NIM':<10} | {'Nama': <12} | {'Nilai': >5}") #mengatur indentasi
    print("-" * 32)

    '''
    untuk tampilan yang rapi, atur f0string formating
    {'NIM':<10} artinya:
    tampilkan nim <= rata kiri dengan lebar 10 karakter
    {'nama':<12}
    tampilan nama rata kiri, dengan lear kolom 12 karakter
    {'nilai':<5}
    tampilan nilai >= rata kanan, lebar kolom 5 karakter
    '''

    for nim in sorted(data_dict):
        nama=data_dict[nim]["nama"]
        nilai=data_dict[nim]["nilai"]
        print(f"{nim: <10} | {nama: <12} | {nilai: <5}")

#memanggil fungsi menampilkan data
tampilkan_data(buka_data)

#================================================
#Praktikum 2 : Konsep ADT dan file handling(STUDI KASUS)
#Latihan 3: membuat fungsi mencari data
#================================================

def cari_data(data_dict):
    #mencari data mahasiswa berdasarkna NotImplemented
    nim_cari = input("NIM mahasiswa yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nim = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("\n=== Data Mahasiswa ====")
        print(f"NIM     : {nim_cari}")
        print(f"Nama    : {nama}")
        print(f"Nilai   : {nilai}")
    else:
        print("\nData tidak ditemukan")


#================================================
#Praktikum 2 : Konsep ADT dan file handling(STUDI KASUS)
#Latihan 4: membuat fungsi update nilai
#================================================

def update_nilai(data_dict):

    #cari nama mahasisiwa yang akan diupdate nilainya
    nim = input("masukkan Nim mahasiswa yang akan diupdate nilainya").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan, update dibatalkan")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru (0-100): "))
    except ValueError:
        print("Nilai harus berupa angka, update dibatalkan")
        return
    
    if nilai_baru <0 or nilai_baru >100:
        print("Nilai harus diantara 0 sampai 100, update dibatalkan")

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"]=nilai_baru
                   
    print(f"update berhasil. nilai{nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

update_nilai(buka_data)

#================================================
#Praktikum 2 : Konsep ADT dan file handling(STUDI KASUS)
#Latihan 5: membuat fungsi menyimpan perubahan data 
#================================================

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8")as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]['nama']
            nilai = data_dict[nim]['nilai']
            file.write(f"{nim}, {nama}, {nilai}\n")
simpan_data(nama_file, buka_data)
print("Data berhasil disimpan")

#================================================
#Praktikum 2 : Konsep ADT dan file handling(STUDI KASUS)
#Latihan 6: membuat menu program
#================================================

def main():

    #menjalankan fungsi 1 load data
    buka_data = baca_data_mahasiswa(nama_file)

while True:
    print("\n===MENU DATA MAHASISWA===") #fungsi pertama
    print("1. Tampilkan semua data") #manggil fungsi nomor 2
    print("2. Cari data brdsarkan NIM") #manggil fungsi nomor 3
    print("3. Update nilai mahasiswa") 
    print("4. Simpan data ke file")
    print("0. Keluar")

    pilihan = input ("Pilihan menu: ").strip()

    if pilihan == "1":
        tampilkan_data(buka_data)

    elif pilihan == "2":
        cari_data(buka_data)
    elif pilihan == "3":
        update_nilai(buka_data)
    elif pilihan == "4":
        simpan_data(nama_file, buka_data)
        print("data berhasil disimpan")

    elif pilihan == "0":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid. Coba lagi")

if __name__ == "__main__":
    main()

