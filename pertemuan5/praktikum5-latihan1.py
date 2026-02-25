#================================================================
#Nama    : Najla Septian Putri
#NIM     : J0403251010
#Kelas   : B/P1
#================================================================

#================================================================
#Latihan 1: Rekursi Pangkat
#================================================================

def pangkat(a, n):

    # Base case
    if n == 0:
        return 1
    
    # Recursive case
    return a * pangkat(a, n - 1)

print(pangkat(2, 4)) # Output: 16


#================================================================
#Jawaban => alur program serta base case dan recursive call.
#================================================================

#1. Alur program:
    #Fungsi pangkat menerima dua parameter. a sebagai bilangan dasar dan n sebagai pangkat.
    #Jika n tidak sama dengan 0, fungsi akan mengalikan a dengan hasil pangkat(a, n-1).
    #Proses ini terus berulang sampai n menjadi 0.
    #Saat n == 0, fungsi berhenti dan mengembalikan 1.
    #Setelah mencapai base case, hasil dikembalikan satu per satu ke atas hingga hasil akhir diperoleh
#2. Base case
    #if n == 0: return 1
    #Base case menghentikan rekursi. Tanpa kondisi ini, fungsi akan terus memanggil dirinya sendiri dan menyebabkan error.
#3. Recursive call
    #return a * pangkat(a, n - 1)
    #Masalah diperkecil dengan mengurangi nilai n sebanyak 1 setiap pemanggilan.
#4. Contoh alur pangkat(2,4):
    #2 × pangkat(2,3)
    #2 × 2 × pangkat(2,2)
    #2 × 2 × 2 × pangkat(2,1)
    #2 × 2 × 2 × 2 × pangkat(2,0)
    #2 × 2 × 2 × 2 × 1 = 16