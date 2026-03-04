#================================================================
# Nama    : Najla Septian Putri
# NIM     : J0403251010
# Kelas   : B/P1
#================================================================

#================================================================
# Latihan 2
#================================================================

def insertion_sort_ascending(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        #KONDISI ASCENDING: data[j] > key 
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

def insertion_sort_descending(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        #KONDISI DESCENDING: data[j] < key 
        while j >= 0 and data[j] < key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

# Contoh eksekusi:
angka = [5, 2, 4, 6, 1, 3]
print("Ascending:", insertion_sort_ascending(angka.copy()))
print("Descending:", insertion_sort_descending(angka.copy()))

#JAWABAN:
#1. Lengkapi kondisi agar menjadi sorting ascending:
#   (terlampir diatas)
#2. Ubah agar menjadi descending:
#   (terlampir diatas)