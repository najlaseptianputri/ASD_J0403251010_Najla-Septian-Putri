#=============================================================
# Nama   : Najla Septian Putri
# NIM    : J0403251010
# Kelas  : B/P1
# Implementasi Dasar Graph
#=============================================================

# Representasi graph menggunakan dictionary
graph = {
    'A':['B','C'],
    'B':['A','D'],
    'C':['A','B'],
    'D':['B','C']

}

# Menampilkan struktur graphS
for node in graph:
    print(node,"=>", graph[node])

# ======================================================================
# PENJELASAN
# ======================================================================
# Graph adalah struktur data yang digunakan untuk merepresentasikan hubungan antar objek.
# Graph terdiri dari simpul (node) dan sisi (edge) yang menghubungkan simpul-simpul tersebut.
# Dalam contoh di atas, kita menggunakan dictionary untuk merepresentasikan graph,
# Dimana setiap kunci adalah sebuah node dan nilainya adalah daftar tetangga (neighbor) dari node tersebut.
# Contoh di atas merepresentasikan sebuah graph sederhana dengan 4 node (A, B, C, D) dan hubungan antar node yang ditunjukkan oleh daftar tetangga.
# Output dari kode di atas akan menampilkan struktur graph yang telah dibuat.