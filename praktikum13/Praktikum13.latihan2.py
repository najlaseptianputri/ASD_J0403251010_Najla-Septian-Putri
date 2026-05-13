#-------------------------------------------------------
# Nama      : Najla Septian Putri
# NIM       : J0403251010 
# Kelas     : B/P1
# Latihan 2
# Praktikum 13 - Graph III: Spanning Tree
#-------------------------------------------------------
# Implementasi Sederhana Algoritma Kruskal 
#-------------------------------------------------------

# Graph direpresentasikan dalam bentuk Edge List (Daftar Sisi).
# Setiap tuple berisi (bobot, node_asal, node_tujuan).
# Menaruh bobot di indeks pertama sangat krusial agar fungsi sort() otomatis 
# mengurutkan berdasarkan nilai bobot tersebut.
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
# Inilah inti dari strategi "Greedy" Kruskal: Ambil yang termurah dulu.
edges.sort()

# Inisialisasi variabel untuk menyimpan hasil
mst = []            # Menampung sisi-sisi yang terpilih masuk MST
total_weight = 0    # Menghitung total akumulasi bobot
connected = set()   # Menggunakan Set untuk melacak node yang sudah terhubung

# Proses iterasi melalui daftar sisi yang sudah terurut
for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))  # Menambahkan sisi ke dalam list MST
        total_weight += weight      # Menambahkan bobot ke total
        
        # Masukkan kedua simpul ke dalam set agar ditandai sebagai 'sudah terhubung'
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree (Latihan Kruskal):")
for edge in mst:
    print(edge)
print("Total bobot =", total_weight)

#-------------------------------------------------------
# JAWABAN ANALISIS
# 1. Edge mana yang dipilih pertama kali? Edge ('C', 'D') dengan bobot 1.
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu? Karena strategi 
#    Kruskal adalah Greedy secara global untuk meminimalkan total bobot seluruh tree.
# 3. Berapa total bobot MST yang dihasilkan? Total bobot adalah 6.
# 4. Mengapa edge tertentu tidak dipilih? Edge seperti ('A', 'B') atau ('A', 'D') 
#    tidak dipilih karena jika ditambahkan akan membentuk cycle atau karena semua 
#    node sudah terhubung dengan bobot yang lebih efisien.
#-------------------------------------------------------