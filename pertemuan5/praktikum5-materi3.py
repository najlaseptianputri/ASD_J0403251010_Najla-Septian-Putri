#================================================================
#Nama   : Najla Septian Putri
#NIM    : J0403251010
#Kelas  : B/P1
#================================================================

#================================================================
#Materi rekursif : Menjumlahkann Elemen List
#================================================================

def jumlah_list(data, index=0):
    #base case
    if index == len(data):
        return 0
    
    #recursive case
    return data[index] + jumlah_list(data, index+1)

print("====Program Jumlah Data List====")
print(jumlah_list([2,4,5]))
