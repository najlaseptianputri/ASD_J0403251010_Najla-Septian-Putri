#=====================================================================
# Nama      : Najla Septian Putri
# NIM       : J0403251010
# Kelas     : B/P1
# Latihan 4 : Membuat BST yang Tidak Seimbang 
#=====================================================================

# Class Node untuk menyimpan data BST 
class Node: 
    """
    Kelas Node mendefinisikan struktur dasar pohon.
    Komentar Diskusi: Struktur ini bersifat dinamis. Memori hanya dialokasikan
    ketika Node baru dibuat, berbeda dengan array yang ukurannya statis.
    """
    def __init__(self, data): 
        self.data = data      # nilai pada node 
        self.left = None      # child kiri 
        self.right = None     # child kanan 

# Fungsi insert untuk BST 
def insert(root, data): 
    """
    ALUR DISKUSI FUNGSI INSERT:
    Fungsi ini bekerja secara rekursif. Kelemahan utama fungsi insert standar 
    adalah ia tidak melakukan pengecekan keseimbangan (balancing). 
    Ia hanya mengikuti aturan: kecil ke kiri, besar ke kanan.
    """
    # Jika root kosong, buat node baru 
    if root is None: 
        return Node(data) 
 
    # Jika data lebih kecil, masuk ke subtree kiri 
    if data < root.data: 
        root.left = insert(root.left, data) 
 
    # Jika data lebih besar, masuk ke subtree kanan 
    elif data > root.data: 
        root.right = insert(root.right, data) 
 
    return root 

# Fungsi preorder untuk melihat urutan data (Root-Left-Right)
def preorder(root): 
    """
    ALUR DISKUSI PREORDER (Root -> Left -> Right):
    Pada pohon yang miring ke kanan (skewed right), Preorder akan mencetak
    data sesuai urutan inputnya. Hal ini terjadi karena tidak ada cabang kiri
    yang perlu dikunjungi.
    """
    if root is not None: 
        print(root.data, end=" ") 
        preorder(root.left) 
        preorder(root.right) 

# Fungsi untuk menampilkan visualisasi struktur hierarki tree 
def tampil_struktur(root, level=0, posisi="Root"): 
    """
    ALUR DISKUSI VISUALISASI:
    Fungsi ini sangat membantu untuk melihat 'kedalaman' (depth) sebuah pohon.
    Semakin banyak indentasi (spasi), semakin dalam posisi node tersebut.
    """
    if root is not None: 
        # Membuat spasi berdasarkan kedalaman level
        indent = "   " * level 
        print(f"{indent}{posisi}: {root.data}") 
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# ----------------------------- 
# Program Utama
# ----------------------------- 
if __name__ == "__main__":
    root = None 
    
    # Memasukkan data secara berurutan agar pohon tidak seimbang
    data_list = [10, 20, 30] 
    
    for data in data_list: 
        root = insert(root, data) 

    print("Preorder BST:") 
    preorder(root) 
    
    print("\n\nStruktur BST:") 
    tampil_struktur(root)

# ---------------------------------------------------------------------
# PENJELASAN
# ---------------------------------------------------------------------
# Data input: [10, 20, 30] (Urutan Naik / Ascending)
#
# ANALISIS STRUKTUR:
# 1. Input 10: Menjadi Root.
# 2. Input 20: Lebih besar dari 10 -> Jadi anak KANAN dari 10.
# 3. Input 30: Lebih besar dari 10, lebih besar dari 20 -> Jadi anak KANAN dari 20.
#
# KESIMPULAN :
# - Pohon ini disebut "Right-Skewed Binary Tree".
# - Pohon ini secara fungsional berubah menjadi Linked List.
# - Efisiensi pencarian (Search) menurun dari O(log n) menjadi O(n). 
#   Artinya, jika kita punya 1.000 data berurutan, kita harus melewati 
#   1.000 langkah untuk mencari data terakhir, bukan 10 langkah (log 1000).
# - Solusi ke depannya adalah menggunakan balancing (seperti di Latihan 6).
# ---------------------------------------------------------------------