#-------------------------------------------------------
# Nama      : Najla Septian Putri
# NIM       : J0403251010 
# Kelas     : B/P1
# Latihan 4 : Membuat Traversal Inorder
#-------------------------------------------------------

# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data    # menyimpan nilai node
        self.left = None    # child kiri
        self.right = None   # child kanan

# membuat fungsi inorder : Left -> Root -> Right
def inorder(node):
    if node is not None:
        inorder(node.left)           # Kunjungi anak kiri
        print(node.data, end=" ")    # Cetak Root (Data)
        inorder(node.right)          # Kunjungi anak kanan

# --- Membuat Tree ---
root = Node("A")

# membuat child level 1
root.left = Node("B")
root.right = Node("C")

# membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# menjalankan transversal inorder
print("Hasil Transversal Inorder:")
inorder(root)


#Penjelasan: 
# 1. Konsep Inorder: Traversal Inorder adalah salah satu teknik penelusuran 
#    pohon biner yang mengunjungi node dengan urutan: Anak Kiri -> Root -> Anak Kanan.
#
# 2. Alur Kerja Rekursif:
#    - Pertama, fungsi akan terus masuk ke cabang kiri terdalam (hingga mencapai leaf).
#    - Kedua, fungsi mencetak data node tersebut (Root lokal).
#    - Ketiga, fungsi baru akan berpindah mengunjungi cabang sebelah kanan.
#
# 3. Urutan pada Binary Search Tree (BST): Dalam materi struktur data, 
#    metode Inorder sangat penting karena jika diterapkan pada Binary Search Tree, 
#    hasil outputnya akan selalu terurut secara alfabetis atau numerik.
#
# 4. Analisis Output: Untuk pohon pada kode ini, urutannya adalah D B E A C.
#    - Program menuju kiri terjauh yaitu D (Cetak D).
#    - Naik ke induknya yaitu B (Cetak B).
#    - Menuju anak kanan dari B yaitu E (Cetak E).
#    - Sisi kiri utama selesai, naik ke root tertinggi yaitu A (Cetak A).
#    - Terakhir, menuju sisi kanan yaitu C (Cetak C).
#
# 5. Pentingnya Base Case: Kondisi 'if node is not None' memastikan bahwa 
#    ketika program mencapai ujung pohon (None), fungsi akan berhenti memanggil 
#    dirinya sendiri dan kembali (backtrack) ke node sebelumnya.