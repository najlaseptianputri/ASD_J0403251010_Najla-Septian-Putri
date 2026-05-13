#-------------------------------------------------------
# Nama      : Najla Septian Putri
# NIM       : J0403251010 
# Kelas     : B/P1
# Latihan 3 
# Praktikum 13 - Graph III: Spanning Tree
#-------------------------------------------------------
# Implementasi Algoritma Prim 
#-------------------------------------------------------

import heapq

# Menggunakan Adjacency List (Daftar Ketetanggaan) dalam bentuk Dictionary.
# Memudahkan pencarian tetangga dari simpul tertentu secara langsung.
# Graph 
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    # 'visited' menyimpan node yang sudah masuk ke dalam struktur MST
    visited = set([start])

    # 'edges' adalah Priority Queue (Heap) untuk menyimpan kandidat sisi berikutnya.
    edges = []

    # Inisialisasi: Masukkan semua sisi yang terhubung dengan node awal (start) ke heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []            # List untuk menyimpan sisi-sisi yang terpilih
    total_weight = 0    # Akumulator untuk total bobot MST

    # Proses utama: Selama masih ada sisi kandidat dalam heap
    while edges:
        # Ambil sisi dengan bobot terkecil dari heap (Greedy Step)
        weight, u, v = heapq.heappop(edges)

        # Cek apakah simpul tujuan (v) sudah pernah dikunjungi
        if v not in visited:
            visited.add(v)              # Tandai simpul v sebagai sudah dikunjungi
            mst.append((u, v, weight))  # Masukkan sisi ke dalam daftar MST
            total_weight += weight      # Tambahkan bobot ke total

            # Tambahkan semua tetangga dari simpul baru (v) ke dalam heap
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    # Hanya tambahkan tetangga yang belum masuk MST
                    heapq.heappush(edges, (w, v, neighbor))
    return mst, total_weight
# Menjalankan fungsi Prim dimulai dari Node 'A'
mst, total = prim(graph, 'A')

print("Minimum Spanning Tree (Latihan Prim):")
for edge in mst:
    print(edge)
print("Total bobot =", total)

#-------------------------------------------------------
# JAWABAN ANALISIS
# 1. Node awal apa yang digunakan? Node 'A'.
# 2. Edge mana yang dipilih pertama kali? Edge ('A', 'C') dengan bobot 2.
# 3. Bagaimana Prim menentukan edge berikutnya? Dengan mencari edge dengan bobot 
#    terkecil yang menghubungkan node yang sudah dikunjungi dengan node yang belum dikunjungi.
# 4. Berapa total bobot MST yang dihasilkan? 6.
# 5. Apa perbedaan pendekatan Prim dan Kruskal? Kruskal memilih edge terkecil secara global 
#    dari seluruh graph, sedangkan Prim membangun tree secara bertahap mulai dari satu node.
#-------------------------------------------------------