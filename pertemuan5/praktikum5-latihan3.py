#================================================================
#Nama    : Najla Septian Putri
#NIM     : J0403251010
#Kelas   : B/P1
#================================================================

#================================================================
#Latihan 3: Mencari Nilai Maksimum
#================================================================

def cari_maks(data, index=0):

    #Base case
    if index == len(data) - 1:
        return data[index]

    #Recursive case
    maks_sisa = cari_maks(data, index + 1)

    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))


#================================================================
#Jawaban => Jelaskan alur program serta base case dan recursive call.
#================================================================

#1. Alur program:
    #Fungsi cari_maks membandingkan elemen saat ini dengan maksimum sisa elemen.
    #Fungsi memanggil dirinya dengan index + 1.
    #Proses terus berjalan sampai mencapai elemen terakhir.
#2. Base case
    #if index == len(data) - 1: return data[index]
    #Artinya jika sudah di elemen terakhir, maka elemen tersebut adalah maksimum sementara.
#3. Recursive call
    #maks_sisa = cari_maks(data, index + 1)
    #Masalah diperkecil dengan menggeser index ke kanan.

#4. Cara kerja:
    #Fungsi bergerak sampai elemen terakhir.
    #Setelah itu, perbandingan dilakukan saat fungsi kembali.
    #Setiap elemen dibandingkan dengan maksimum dari sisa list.
    #Hasil terbesar dikembalikan ke atas.
#5. Contoh pada [3,7,2,9,5]
    #Akan membandingkan dari belakang ke depan sampai didapat 9 sebagai nilai maksimum.