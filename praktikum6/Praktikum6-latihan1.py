#================================================================
# Nama    : Najla Septian Putri
# NIM     : J0403251010
# Kelas   : B/P1
#================================================================

#================================================================
# Latihan 1
#================================================================

def insertion_sort(data):
    #Perulangan dimulai dari indeks 1 hingga panjang data
    for i in range(1, len(data)):
        key = data[i] # Elemen yang akan disisipkan
        j = i - 1 # Menunjuk ke elemen sebelumnya
        
        #Geser elemen yang lebih besar dari key ke kanan 
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        
        #Tempatkan key pada posisi yang benar
        data[j + 1] = key
    return data

# JAWABAN 
# 1. Mengapa perulangan dimulai dari indeks 1? 
#    Karena elemen pertama (indeks 0) dianggap sudah terurut sebagai dasar perbandingan awal.
# 2. Apa fungsi variabel key? 
#    Variabel 'key' menyimpan nilai elemen yang sedang diproses untuk dibandingkan dan 
#    disisipkan ke posisi yang tepat pada bagian list yang sudah terurut.
# 3. Mengapa digunakan while, bukan for? 
#    Karena jumlah pergeseran elemen ke kiri tidak tetap (tergantung kondisi data[j] > key). 
#    While lebih fleksibel untuk berhenti saat kondisi urutan sudah terpenuhi.
# 4. Operasi apa yang terjadi di dalam while? 
#    Operasi pergeseran (shifting), di mana elemen yang lebih besar digeser satu posisi ke kanan 
#    untuk memberi ruang bagi variabel 'key'.