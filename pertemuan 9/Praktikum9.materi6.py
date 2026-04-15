#-------------------------------------------------------
# Nama      : Najla Septian Putri
# NIM       : J0403251010 
# Kelas     : B/P1
# Latihan 6 : Struktur Organisasi Perusahaan
#-------------------------------------------------------

# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data    # menyimpan nilai node
        self.left = None    # child kiri
        self.right = None   # child kanan

# Menambahkan fungsi preorder agar program bisa berjalan
def preorder(node):
    if node is not None:
        print(node.data)            # Cetak data node (Root)
        preorder(node.left)         # Kunjungi cabang kiri
        preorder(node.right)        # Kunjungi cabang kanan

# --- Membuat Tree Struktur Organisasi ---
root = Node("Direktur")

# child level 1 (Bawahan langsung Direktur)
root.left = Node("Manajer A")
root.right = Node("Manajer B")

# child level 2 (Bawahan Manajer)
root.left.left = Node("Staff1")
root.right.left = Node("Staff2")
root.right.right = Node("Staff3")

# Menjalankan transversal preorder
print("Struktur organisasi (preorder):")
preorder(root)


#Penjelasan :
# 1. Penerapan Real-World: Latihan ini menunjukkan bahwa struktur data Tree 
#    sangat efektif untuk merepresentasikan hierarki nyata, seperti jabatan 
#    di perusahaan di mana satu atasan bisa memiliki beberapa bawahan.
#
# 2. Terminologi Hierarki:
#    - Root: Diwakili oleh 'Direktur' sebagai puncak pimpinan.
#    - Parent Node: 'Manajer A' dan 'Manajer B' yang memiliki bawahan langsung.
#    - Leaf Node: 'Staff1', 'Staff2', dan 'Staff3' karena berada di posisi 
#      paling bawah dan tidak memiliki bawahan lagi dalam sistem ini.
#
# 3. Struktur Cabang: 
#    - Manajer A memiliki struktur asimetris (hanya memiliki satu Staff di kiri).
#    - Manajer B memiliki struktur penuh (memiliki Staff di kiri dan kanan).
#
# 4. Relevansi Preorder Traversal: Dalam kasus organisasi, metode Preorder 
#    (Root-Left-Right) adalah yang paling logis digunakan karena urutan 
#    pembacaannya dimulai dari Jabatan Tertinggi baru kemudian turun ke 
#    Level di bawahnya secara berurutan.
#
# 5. Hasil Penelusuran: Output program akan menampilkan alur komando dari 
#    Direktur -> Manajer A -> Staff1 -> Manajer B -> Staff2 -> Staff3.