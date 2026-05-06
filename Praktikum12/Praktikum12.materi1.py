#================================================================
# Nama  : Najla Septian Putri
# NIM   : J0403251010
# Kelas : B/P1
# Praktikum 12 - Graph II: Shortest Path
#================================================================

import heapq

# Representasi graph berbobot menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    # Menyimpan jarak minimum, diatur menjadi tak hingga (infinity) di awal
    distances = {node: float('inf') for node in graph}
    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0
    # Priority queue untuk menyimpan node yang akan dieksplorasi beserta jaraknya
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Periksa semua tetangga dari node yang sedang dieksplorasi
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # Jika jarak baru lebih kecil dari jarak yang tercatat sebelumnya, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return distances

hasil = dijkstra(graph, 'A')
print(hasil)

# ==========================================================
# PENJELASAN 
# ==========================================================
# 1. Tujuan Program: 
#    Program ini mengimplementasikan algoritma Dijkstra untuk mencari 
#    jalur/jarak terpendek dari satu titik awal (start node 'A') ke 
#    semua titik lainnya di dalam graf yang berbobot positif.
#
# 2. Cara Kerja Algoritma:
#    - Inisialisasi: Semua jarak awal (distances) diatur menjadi tak terhingga 
#      (float('inf')), kecuali node awal yang diatur menjadi 0.
#    - Priority Queue: Program menggunakan modul 'heapq' (antrean prioritas) 
#      untuk selalu memilih dan memproses node dengan jarak sementara paling kecil. 
#      Pendekatan ini disebut pendekatan serakah (Greedy).
#    - Relaksasi: Pada setiap iterasi, program mengecek semua tetangga dari node 
#      saat ini. Jika total jarak ke tetangga melalui node saat ini ternyata 
#      lebih pendek (lebih kecil) daripada jarak yang tercatat sebelumnya, 
#      maka jarak tersebut diperbarui.
#
# 3. Keterbatasan: 
#    Algoritma Dijkstra sangat cepat dan efisien untuk graf dengan bobot positif, 
#    namun algoritma ini bisa menghasilkan perhitungan yang salah jika diterapkan 
#    pada graf yang memiliki bobot/edge bernilai negatif.