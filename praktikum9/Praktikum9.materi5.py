#-------------------------------------------------------
# Nama      : Najla Septian Putri
# NIM       : J0403251010 
# Kelas     : B/P1
# Latihan 5 : Membuat Traversal Postorder
#-------------------------------------------------------

# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data    # menyimpan nilai node
        self.left = None    # child kiri
        self.right = None   # child kanan

# membuat fungsi Postorder : Left -> Right -> Root
def Postorder(node):
    if node is not None:
        Postorder(node.left)           # Kunjungi anak kiri
        Postorder(node.right)          # Kunjungi anak kanan
        print(node.data, end=" ")      # Cetak Root (Data)

# --- Membuat Tree ---
root = Node("A")

# membuat child level 1
root.left = Node("B")
root.right = Node("C")

# membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# menjalankan transversal Postorder
print("Hasil Transversal Postorder:")
Postorder(root)


#Penjelasan: 
# 1. Konsep Postorder: Traversal Postorder adalah teknik penelusuran pohon 
#    biner yang mengunjungi node dengan urutan: Anak Kiri -> Anak Kanan -> Root.
#
# 2. Karakteristik Utama: Ciri khas dari metode ini adalah Root utama akan 
#    selalu diproses paling terakhir. Program memastikan seluruh anak (sub-tree) 
#    sudah selesai dikunjungi sebelum mencetak data induknya.
#
# 3. Alur Kerja Rekursif:
#    - Program menelusuri cabang kiri sampai habis.
#    - Program menelusuri cabang kanan pada level yang sama.
#    - Program mencetak data node (Root) tersebut.
#
# 4. Analisis Output: Untuk pohon pada kode ini, urutannya adalah D E B C A.
#    - Kunjungi D (Kiri dari B).
#    - Kunjungi E (Kanan dari B).
#    - Cetak B (Root dari D dan E).
#    - Kunjungi C (Kanan dari A).
#    - Terakhir, cetak A (Root utama).
#
# 5. Kegunaan Praktis: Traversal Postorder sangat sering digunakan untuk 
#    proses penghapusan pohon (menghapus anak sebelum induk) atau untuk 
#    mengevaluasi ekspresi matematika dalam notasi Postfix (Reverse Polish Notation).