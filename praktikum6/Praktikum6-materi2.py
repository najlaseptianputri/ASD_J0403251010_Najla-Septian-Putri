#================================================================
#Nama    : Najla Septian Putri
#NIM     : J0403251010
#Kelas   : B/P1
#================================================================

#================================================================
#Materi 2: Insertion Sort dengan Tracing
#================================================================

def insertion_sort(data):

    #melihat data awal
    print("Data Awal: ", data)
    print("="*50)

    #buat suatu Looping mulai dari data ke 2(index array ke 1)
    for i in range(1, len(data)):

        key = data[i]   #simpan nilai yang disisipkan 
        j = i-1     #index elemen terakhir dibagian kiri

        print("Iterasi ke- ", i)
        print("Nilai Key = ", key)
        print("Bagian Kiri (terurut): ", data[:i])
        print("Bagian Kanan(belum terurut): ", data[i:])

        #geser 
        while j>=0  and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        #sisipkan key ke posisi yang benar
        data[j+1] = key

        print("Setelah disisipkan :", data)
        print("="*50)
    return data

angka = [7,8,5,2,4,6]
print("Hasil Sorting: ", insertion_sort(angka))

