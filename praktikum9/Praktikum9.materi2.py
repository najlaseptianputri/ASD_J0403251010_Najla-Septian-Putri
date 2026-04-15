#-------------------------------------------------------
# Nama      : Najla Septian Putri
# NIM       : J0403251010 
# Kelas     : B/P1
# Latihan 2 : Membuat node Tree
#-------------------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data    # menyimpan nilai node
        self.left = None    # child kiri
        self.right = None   # child kanan

# --- Membangun Struktur Tree ---

# Membuat root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2 
root.left.left = Node("D")
root.left.right = Node("E")

# Lanjutan: Membuat child level 2 
root.right.left = Node("F")   # Anak kiri dari C
root.right.right = Node("G")  # Anak kanan dari C

# --- Menampilkan Isi Node ---
print("Data pada root:", root.data)
print("Data child kiri root (B):", root.left.data)
print("Data child kanan root (C):", root.right.data)

print("\n--- Sisi Kiri (Subtree B) ---")
print("Data child kiri dari B (D):", root.left.left.data)
print("Data child kanan dari B (E):", root.left.right.data)

print("\n--- Sisi Kanan (Subtree C) ---")
print("Data child kiri dari C (F):", root.right.left.data)
print("Data child kanan dari C (G):", root.right.right.data)


#Penjelasan:
# 1. Pembentukan Struktur Bertingkat: Program ini menunjukkan cara membangun 
#    pohon biner yang lebih kompleks dengan menambahkan 'Child' pada setiap 
#    node yang ada (Level 1 dan Level 2).
#
# 2. Hubungan Parent-Child-Grandchild: 
#    - Node A adalah Root (Induk Utama).
#    - Node B dan C adalah Child dari A, sekaligus menjadi Parent bagi node di bawahnya.
#    - Node D, E, F, dan G adalah Leaf Nodes (Simpul Daun) atau cucu dari Root A.
#
# 3. Pengalamatan Node (Chaining): Untuk mengakses node di level yang lebih dalam, 
#    kita menggunakan titik (dot notation) sebagai jalur penelusuran. 
#    Contoh: 'root.right.left' berarti kita bergerak dari Root -> ke Kanan (C) 
#    -> lalu ke Kiri untuk mencapai Node F.
#
# 4. Leaf Nodes (Simpul Daun): Simpul D, E, F, dan G disebut Leaf Nodes karena 
#    atribut 'left' dan 'right' mereka bernilai 'None', yang menandakan akhir 
#    dari sebuah cabang dalam pohon biner.
#
# 5. Akses Objek vs Data: Untuk mencetak nilai yang tersimpan, kita harus 
#    mengakses atribut '.data'. Tanpa atribut ini, Python hanya akan menampilkan 
#    lokasi penyimpanan objek di memori, bukan isi datanya.