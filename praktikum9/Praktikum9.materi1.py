#-------------------------------------------------------
# Nama      : Najla Septian Putri
# NIM       : J0403251010 
# Kelas     : B/P1
# Latihan 1 : Membuat node (dasar Binary Tree)
#-------------------------------------------------------


#class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data    # menyimpan nilai node
        self.left = None    # child kiri
        self.right = None   # child kanan

# Membuat root (Harus sejajar dengan 'class', bukan di dalam class)
root = Node("A")

# Menampilkan isi node
print("Data pada root:", root.data)
print("Data child kiri root:", root.left)
print("Data child kanan root:", root.right)


#Penjelasan :
# 1. Definisi Node: Program ini mengimplementasikan class Node sebagai unit 
#    terkecil dalam Pohon Biner. Node berfungsi sebagai wadah untuk menyimpan 
#    data dan menghubungkan diri dengan elemen lainnya dalam hierarki.
#
# 2. Atribut Konstruktor (__init__):
#    - self.data  : Menyimpan nilai utama (dalam hal ini karakter "A").
#    - self.left  : Berfungsi sebagai pointer (penunjuk) ke cabang sebelah kiri.
#    - self.right : Berfungsi sebagai pointer (penunjuk) ke cabang sebelah kanan.
#
# 3. Konsep Root: Objek 'root' adalah titik akses utama atau simpul akar dari 
#    pohon biner. Semua penelusuran data akan selalu dimulai dari root ini.
#
# 4. Status Awal (None): Saat inisialisasi, nilai 'left' dan 'right' diatur 
#    sebagai 'None'. Ini menunjukkan bahwa pada awal pembuatan, node tersebut 
#    masih berdiri sendiri dan belum memiliki anak (child).
#
# 5. Output Program: Data pada root menampilkan nilai objek, sedangkan child 
#    kiri dan kanan menampilkan 'None', yang menandakan struktur pohon saat 
#    ini hanya terdiri dari satu node tunggal.
