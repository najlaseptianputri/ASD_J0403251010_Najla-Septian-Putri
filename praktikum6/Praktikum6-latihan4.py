#================================================================
# Nama    : Najla Septian Putri
# NIM     : J0403251010
# Kelas   : B/P1
#================================================================

#================================================================
# Latihan 4
#================================================================

def merge_sort(data):
    #Base case
    if len(data) <= 1:
        return data
    
    #Divide
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    
    #Recursive call 
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    return merge(left_sorted, right_sorted) 

# JAWABAN:
#1. Apa yang dimaksud dengan base case?
#    Kondisi berhenti dalam rekursi. Pada Merge Sort, base case terjadi saat 
#    list memiliki 0 atau 1 elemen, karena list tersebut sudah dianggap terurut.
#2. Mengapa fungsi memanggil dirinya sendiri? 
#    Untuk memecah list besar menjadi sub-list yang lebih kecil secara terus-menerus 
#    (Divide) sampai mencapai base case.
#3. Apa tujuan fungsi merge()? 
#    Untuk menggabungkan kembali dua sub-list yang sudah terurut menjadi satu 
#    list baru yang tetap terurut.