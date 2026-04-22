#=====================================================================
# Nama      : Najla Septian Putri
# NIM       : J0403251010
# Kelas     : B/P1
# Latihan 1 : Membuat Node dan BST 
#=====================================================================

class Node:
    """
    Kelas Node berfungsi sebagai cetak biru (blueprint) untuk setiap elemen dalam pohon.
    Setiap node menyimpan tiga komponen utama:
    1. data  : Nilai yang disimpan dalam node.
    2. left  : Referensi ke anak kiri (nilai yang lebih kecil).
    3. right : Referensi ke anak kanan (nilai yang lebih besar).
    """
    def __init__(self, data): 
        self.data = data
        self.left = None
        self.right = None

#=====================================================================
# Latihan 1: Node dan Insert BST
#=====================================================================

def insert(root, data):
    """
    ALUR LOGIKA FUNGSI INSERT (Rekursif):
    1. Base Case: Jika root kosong (None), fungsi membuat Node baru dan mengembalikannya.
    2. Perbandingan:
       - Jika data baru < data root saat ini, fungsi memanggil dirinya sendiri untuk 
         menuju ke subtree kiri (root.left).
       - Jika data baru > data root saat ini, fungsi memanggil dirinya sendiri untuk 
         menuju ke subtree kanan (root.right).
    3. Penempatan: Proses berulang (rekursif) hingga ditemukan posisi None yang tepat.
    4. Pencegahan Duplikat: Pada kode ini, jika data sudah ada, ia tidak akan dimasukkan ulang.
    """
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data) 
    elif data > root.data:
        root.right = insert(root.right, data)
    
    return root

# Inisialisasi Data
data_list = [50, 30, 70, 20, 40, 80] 
root = None

# Memasukkan data ke dalam BST menggunakan perulangan
for data in data_list:
    root = insert(root, data)

print("BST berhasil dibuat")

#=====================================================================
# Latihan 2: Traversal Inorder 
#=====================================================================

def inorder(root):
    """
    ALUR LOGIKA TRAVERSAL INORDER:
    Traversal ini mengikuti prinsip (Left - Root - Right).
    1. Kunjungi Subtree Kiri: Melakukan rekursif ke kiri sampai node terkecil.
    2. Cetak Root: Mencetak nilai node saat ini.
    3. Kunjungi Subtree Kanan: Melakukan rekursif ke kanan.
    
    KESIMPULAN: 
    Karakteristik unik dari Inorder pada BST adalah output yang dihasilkan 
    akan SELALU terurut secara ascending (dari terkecil ke terbesar).
    """
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

print("\nHasil Inorder (Data Terurut): ") 
inorder(root)

#=====================================================================
# Latihan 3: Searching 
#=====================================================================

def search(root, key):
    """
    ALUR LOGIKA FUNGSI SEARCH:
    Fungsi ini memanfaatkan sifat efisiensi BST (O(log n)):
    1. Jika root None: Berarti data (key) tidak ditemukan di seluruh pohon.
    2. Jika data == key: Data ditemukan! Mengembalikan nilai True.
    3. Jika key < data root: Pencarian hanya dilanjutkan ke sisi kiri, 
       mengabaikan seluruh sisi kanan (mempercepat proses).
    4. Jika key > data root: Pencarian hanya dilanjutkan ke sisi kanan.
    """
    if root is None:
        return False
    
    if root.data == key:
        return True    
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)

# Uji Pencarian
key = 40
if search(root, key):
    print("Hasil: Data Ditemukan")
else:
    print("Hasil: Data Tidak Ditemukan")

#=====================================================================
# PENJELASAN:
# 1. Struktur Node adalah pondasi; tanpa pointer left/right, hirarki tidak terbentuk.
# 2. Fungsi Insert sangat bergantung pada urutan input; jika input terurut, 
#    BST bisa menjadi tidak seimbang (skewed).
# 3. Search pada BST jauh lebih cepat dibanding Linear Search pada List biasa 
#    karena setiap langkah membuang setengah dari kemungkinan jalur pencarian.
#=====================================================================