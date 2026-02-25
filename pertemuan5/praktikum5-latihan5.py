#================================================================
#Nama    : Najla Septian Putri
#NIM     : J0403251010
#Kelas   : B/P1
#================================================================

#================================================================
#Studi Kasus: Generator PIN
#================================================================

def buat_pin(panjang, hasil=""):
    
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)

buat_pin(3)

#================================================================
#Jawaban => Bagaimana cara mencegah angka yang sama muncul berulang.
#================================================================

#Pada kode saat ini:
    #Angka boleh berulang.
    #Contoh 000, 111, 222 tetap muncul.

#Untuk mencegah angka sama muncul berulang, ada dua cara.
    #1. Cara 1. Gunakan pengecekan sebelum rekursi
        #Tambahkan kondisi agar angka tidak digunakan jika sudah ada di hasil.
        #Contoh logika
            #for angka in [“0”,“1”,“2”]:
            #if angka not in hasil:
            #buat_pin(panjang, hasil + angka)

        #Dengan cara ini:
            #Setiap digit hanya dipakai satu kali dalam satu PIN.
            #Ini menghasilkan permutasi tanpa pengulangan.

    #2. Cara 2. Gunakan struktur data set untuk menyimpan angka yang sudah dipakai
        #Tambahkan parameter tambahan seperti used.

        #Kesimpulan:
            #Tanpa pembatasan, total kemungkinan adalah 3^3 = 27.
            #Dengan tanpa pengulangan, total menjadi 3! = 6 kemungkinan.