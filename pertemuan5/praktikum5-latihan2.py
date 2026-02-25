#================================================================
#Nama    : Najla Septian Putri
#NIM     : J0403251010
#Kelas   : B/P1
#================================================================

#================================================================
#Latihan 2: Tracing Rekursi
#================================================================

def countdown(n):

    if n == 0:
        print("Selesai")
        return
    print("Masuk:", n)

    countdown(n - 1)

    print("Keluar:", n)

countdown(3)


#================================================================
#Jawaban => Mengapa output “Keluar” muncul terbalik.
#================================================================

#1. Alur program
    #Fungsi countdown mencetak “Masuk” sebelum memanggil dirinya sendiri.
    #Fungsi terus dipanggil sampai n == 0.
    #Saat n == 0, base case tercapai dan fungsi berhenti.
    #Setelah itu, proses kembali ke pemanggilan sebelumnya.
#2. Mengapa “Keluar” terbalik
    #Karena sifat call stack.
        #“Masuk” dicetak saat fase stacking.
        #Setelah base case, fungsi selesai satu per satu dari bawah ke atas.
        #Proses ini disebut unwinding.
        #Karena kembali dari n kecil ke n besar, maka “Keluar” dicetak dalam urutan terbalik.
#3. Contoh urutan untuk countdown(3)
    #Masuk 3
    #Masuk 2
    #Masuk 1
    #Selesai
    #Keluar 1
    #Keluar 2
    #Keluar 3