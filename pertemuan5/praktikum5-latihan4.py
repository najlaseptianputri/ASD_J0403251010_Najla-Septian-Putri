#================================================================
#Nama    : Najla Septian Putri
#NIM     : J0403251010
#Kelas   : B/P1
#================================================================

#================================================================
#Latihan 4: Kombinasi Huruf
#================================================================

def kombinasi(n, hasil=""):

    if len(hasil) == n:
        print(hasil)
        return
    
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")

kombinasi(2)


#================================================================
#Jawaban => Bagaimana jumlah kombinasi yang dihasilkan.
#================================================================

#1.Alur program
    #Fungsi kombinasi membangun string secara bertahap.
    #Jika panjang hasil sudah sama dengan n, maka dicetak.
    #Setiap langkah memiliki dua pilihan. Tambah A atau tambah B.

#2. Pola choose dan explore
    #Choose A lalu eksplorasi
    #Choose B lalu eksplorasi

    #Jumlah kombinasi
    #Karena setiap posisi memiliki 2 pilihan dan panjang n = 2, maka jumlah kombinasi adalah:
    #2^n

    #Untuk n = 2
    #2^2 = 4 kombinasi

#Hasil
#AA
#AB
#BA
#BB