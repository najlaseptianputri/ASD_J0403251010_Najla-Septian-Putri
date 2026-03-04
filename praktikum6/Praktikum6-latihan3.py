#================================================================
# Nama    : Najla Septian Putri
# NIM     : J0403251010
# Kelas   : B/P1
#================================================================

#================================================================
# Latihan 3
#================================================================

#Data Awal: [5, 2, 4, 6, 1, 3] 

def insertion_sort(data):
    # Algoritma ini membagi list menjadi bagian terurut dan tidak terurut
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        
        # Memindahkan elemen yang lebih besar dari key ke satu posisi di depan
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        
        # Menampilkan proses tracing setiap iterasi
        print(f"Iterasi i={i}: {data}")

# Data yang diminta untuk tracing [cite: 33]
data_latihan = [5, 2, 4, 6, 1, 3]

print("Data awal:", data_latihan)
print("-" * 30)
insertion_sort(data_latihan)
print("-" * 30)
print("Hasil akhir:", data_latihan)

#JAWABAN:
#1. Tuliskan isi list setelah iterasi i=1: 
#    [2, 5, 4, 6, 1, 3] (Angka 2 disisipkan sebelum 5)
#2. Tuliskan isi list setelah iterasi i=3:
#    Iterasi i=1: [2, 5, 4, 6, 1, 3]
#    Iterasi i=2: [2, 4, 5, 6, 1, 3]
#    Iterasi i=3: [2, 4, 5, 6, 1, 3] (6 sudah lebih besar dari 5, posisi tetap)
#    Hasil i=3: [2, 4, 5, 6, 1, 3]
#3. Berapa kali pergeseran terjadi pada iterasi i=4?
#    i=4 adalah angka 1. Angka 1 harus dibandingkan dan menggeser 6, 5, 4, dan 2.
#    Terjadi 4 kali pergeseran.