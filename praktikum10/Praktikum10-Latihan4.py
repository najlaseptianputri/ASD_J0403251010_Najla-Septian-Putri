#=====================================================================
# Nama      : Najla Septian Putri
# NIM       : J0403251010
# Kelas     : B/P1
# Latihan 6 : Rotasi Kanan pada BST Tidak Seimbang
#=====================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#=====================================================================
# PENJELASAN: FUNGSI ROTASI KANAN (Right Rotation)
#=====================================================================
# Rotasi kanan digunakan ketika sebuah node memiliki berat di sisi kiri 
# (Left-Heavy), yang biasanya terjadi jika data dimasukkan secara menurun.
#
# Logika Mekanis Rotasi:
# 1. Tentukan 'x' sebagai anak kiri dari 'y' (root lama). 'x' adalah calon root baru.
# 2. Simpan subtree kanan milik 'x' ke dalam variabel sementara 'T2'. 
#    Ini penting agar data di sisi kanan 'x' tidak terputus.
# 3. Lakukan rotasi: Pindahkan 'y' menjadi anak kanan dari 'x'.
# 4. Hubungkan kembali 'T2' menjadi anak kiri dari 'y'.
# 5. Kembalikan 'x' sebagai root yang baru.
#=====================================================================

# Fungsi untuk melakukan Rotasi Kanan
def rotate_right(y):
    # y adalah node yang tidak seimbang (dalam kasus ini: 30)
    x = y.left        # x menjadi root baru (dalam kasus ini: 20)
    T2 = x.right      # Menyimpan subtree kanan dari x (jika ada)

    # Melakukan rotasi
    x.right = y
    y.left = T2

    # Mengembalikan root yang baru
    return x

# Fungsi insert standar untuk membangun pohon awal
def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root

# Fungsi untuk menampilkan struktur pohon
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        indent = "   " * level
        print(f"{indent}{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# -----------------------------
# Program Utama
# -----------------------------
if __name__ == "__main__":
    root = None
    # Data dimasukkan berurutan turun agar pohon miring ke kiri
    data_list = [30, 20, 10]
    
    for data in data_list:
        root = insert(root, data)

    print("Struktur Sebelum Rotasi Kanan")
    tampil_struktur(root)

    # Melakukan rotasi kanan pada root (node 30)
    root = rotate_right(root)

    print("\nStruktur Sesudah Rotasi Kanan")
    tampil_struktur(root)

#=====================================================================
# PENJELASAN PROGRAM UTAMA:
#=====================================================================
# KASUS SEBELUM ROTASI:
# Input data [30, 20, 10] menghasilkan "Left-Skewed Tree" (pohon miring kiri).
# Struktur: 30 (Root) -> 20 (L) -> 10 (LL).
# Masalah: Pohon tidak efisien karena tinggi (height) maksimal.
#
# KASUS SESUDAH ROTASI:
# Setelah rotate_right(30), node 20 naik menjadi Root.
# Node 10 tetap di kiri (L), dan node 30 berpindah menjadi anak kanan (R).
# Pohon menjadi seimbang sempurna dengan tinggi hanya 2 level.
#=====================================================================