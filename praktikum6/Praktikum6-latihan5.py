#================================================================
# Nama    : Najla Septian Putri
# NIM     : J0403251010
# Kelas   : B/P1
#================================================================

#================================================================
# Latihan 5
#================================================================

def merge(left, right):
    result = []
    i = 0
    j = 0

    #JAWABAN SOAL NOMOR 1:
    #1. Melengkapi kondisi agar ascending
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: # Kondisi ascending 
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    #2. Jelaskan fungsi result.extend()
    #    Fungsi extend() digunakan untuk menambahkan semua elemen yang tersisa 
    #    dari list left atau right ke dalam result setelah salah satu list habis dibandingkan. 
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Uji coba
print(merge([1, 4, 7], [2, 5, 8]))

#JAWABAN:
#1. Lengkapi kondisi agar menjadi ascending:
#   (terlampir di atas)
#2. Jelaskan fungsi result.extend()
#    Fungsi extend() digunakan untuk menambahkan semua elemen yang tersisa 
#    dari list left atau right ke dalam result setelah salah satu list habis dibandingkan.