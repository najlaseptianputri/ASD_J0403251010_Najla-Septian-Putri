#-------------------------------------------------------
# Nama      : Najla Septian Putri
# NIM       : J0403251010 
# Kelas     : B/P1
# Latihan 3 : Membuat Traversal Preorder
#-------------------------------------------------------

# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data    # menyimpan nilai node
        self.left = None    # child kiri
        self.right = None   # child kanan

# fungsi preorder : Root -> Left -> Right
def preorder(node):
    if node is not None:
        print(node.data, end=" ")  # Cetak Root
        preorder(node.left)        # Ke anak kiri
        preorder(node.right)       # Ke anak kanan

# --- Membuat Tree ---
root = Node("A")

# membuat child level 1
root.left = Node("B")
root.right = Node("C")

# membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# menjalankan transversal preorder
print("Hasil Transversal Preorder:")
preorder(root)


#Penjelasan: 
# 1. Konsep Traversal: Traversal adalah proses mengunjungi setiap node 
#    dalam pohon tepat satu kali. Preorder adalah salah satu metode 
#    Depth-First Search (DFS) yang memprioritaskan kunjungan pada akar.
#
# 2. Urutan Penelusuran: Algoritma ini mengikuti aturan Root -> Left -> Right.
#    - Pertama, program mencetak data pada node saat ini (Root).
#    - Kedua, program melakukan rekursi ke cabang kiri sampai mencapai leaf.
#    - Ketiga, program melakukan rekursi ke cabang kanan.
#
# 3. Logika Rekursif: Fungsi 'preorder' memanggil dirinya sendiri. Syarat 
#    'if node is not None' berfungsi sebagai "base case" atau batas berhenti 
#    agar rekursi tidak berjalan selamanya saat mencapai ujung pohon.
#
# 4. Analisis Output: Pada pohon ini, urutan yang dihasilkan adalah A B D E C.
#    - Mulai dari A (Root).
#    - Ke kiri ke B, lalu ke kiri lagi ke D.
#    - Kembali ke B, lalu ke kanan ke E.
#    - Setelah sisi kiri A selesai, baru terakhir ke kanan ke C.
#
# 5. Parameter 'end=" "': Digunakan dalam fungsi print agar hasil cetakan 
#    tampil menyamping dalam satu baris, sehingga memudahkan pembacaan 
#    urutan traversal.