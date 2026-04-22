#=====================================================================
# Nama      : Najla Septian Putri
# NIM       : J0403251010
# Kelas     : B/P1
# Latihan 5 : Rotasi Kiri pada BST Tidak Seimbang  
#=====================================================================

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None 
        self.right = None 
 
# Fungsi preorder untuk melihat isi tree 
def preorder(root): 
    if root is not None: 
        print(root.data, end=" ") 
        preorder(root.left) 
        preorder(root.right) 
 
 
# Fungsi untuk menampilkan struktur tree 
def tampil_struktur(root, level=0, posisi="Root"): 
    if root is not None: 
        print("   " * level + f"{posisi}: {root.data}") 
        tampil_struktur(root.left, level + 1, "L") 
        tampil_struktur(root.right, level + 1, "R") 
 
#=====================================================================
# PENJELASAN: FUNGSI ROTASI KIRI (Left Rotation)
#=====================================================================
# Rotasi kiri dilakukan ketika sebuah node memiliki 'Balance Factor' negatif
# yang berat ke kanan (Right-Heavy). 
#
# Langkah-langkah Mekanis:
# 1. Simpan anak kanan dari node 'x' (root lama) ke dalam variabel 'y'.
# 2. Ampan subtree kiri dari 'y' (yaitu T2) agar tidak hilang saat rotasi.
# 3. Jadikan 'x' sebagai anak kiri dari 'y'.
# 4. Pindahkan T2 menjadi anak kanan dari 'x'.
# 5. Kembalikan 'y' sebagai root baru untuk memperbarui struktur pohon.
#=====================================================================

# Fungsi rotasi kiri 
def rotate_left(x): 
    # x adalah root lama 
    y = x.right       # y (20) adalah child kanan x 
    T2 = y.left       # subtree kiri milik y disimpan sementara 
 
    # Proses rotasi 
    y.left = x        # x (10) menjadi child kiri dari y 
    x.right = T2      # child kanan x diganti dengan T2 
 
    # y(20) menjadi root baru 
    return y

# ----------------------------- 
# Program utama 
# ----------------------------- 
# Membuat tree yang tidak seimbang: 
# 10 -> 20 -> 30 
root = Node(10) 
root.right = Node(20) 
root.right.right = Node(30) 
print("Preorder sebelum rotasi kiri:") 
preorder(root) 
print("\n\nStruktur sebelum rotasi kiri:") 
tampil_struktur(root) 
# Melakukan rotasi kiri pada root 
root = rotate_left(root) 
print("\nPreorder sesudah rotasi kiri:") 
preorder(root) 
print("\n\nStruktur sesudah rotasi kiri:") 
tampil_struktur(root) 

#=====================================================================
# PENJELASAN PROGRAM UTAMA:
#=====================================================================
# KASUS SEBELUM ROTASI:
# Pohon berbentuk Skewed Right (10 -> 20 -> 30).
# Tinggi pohon (height) adalah 3. Operasi pencarian tidak efisien.
#
# KASUS SESUDAH ROTASI:
# Node 20 naik menjadi Root. 
# Node 10 menjadi anak KIRI, dan Node 30 tetap menjadi anak KANAN.
# Pohon menjadi SEIMBANG (Balanced). Tinggi pohon berkurang menjadi 2.
# Efisiensi pencarian meningkat kembali menjadi O(log n).
#=====================================================================
