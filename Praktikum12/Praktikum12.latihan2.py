#================================================================
# Nama      : Najla Septian Putri
# NIM       : J0403251010
# Kelas     : B/P1
# Praktikum 12 - Graph II: Shortest Path
# Latihan 2 : Implementasi Dijkstra
#================================================================

import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat, proses dilewati
        if current_distance > distances[current_node]:
            continue
            
        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

hasil = dijkstra(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# ==========================================================
# Jawaban Analisis:
# 1. Berapa jarak terpendek dari A ke B?
#    Jawab: 4
# 2. Berapa jarak terpendek dari A ke C?
#    Jawab: 2
# 3. Berapa jarak terpendek dari A ke D?
#    Jawab: 3
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
#    Jawab: Karena total bobot (biaya) jalur A -> C -> D adalah 2 + 1 = 3, yang jauh lebih kecil dibandingkan rute A -> B -> D yang memiliki total bobot 4 + 5 = 9.
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
#    Jawab: Priority queue berfungsi untuk selalu memilih dan memproses node dengan jarak sementara paling kecil secara efisien (greedy approach) pada setiap iterasinya.
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
#    Jawab: Algoritma Dijkstra mengasumsikan bahwa jarak minimum yang sudah ditemukan tidak akan berubah (pendekatan greedy). Jika terdapat edge dengan bobot negatif, jalur yang telah "difinalisasi" mungkin bisa menjadi lebih kecil di iterasi selanjutnya, sehingga Dijkstra dapat menghasilkan perhitungan jarak yang salah.