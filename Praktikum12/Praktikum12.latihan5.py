#================================================================
# Nama      : Najla Septian Putri
# NIM       : J0403251010
# Kelas     : B/P1
# Praktikum 12 - Graph II: Shortest Path
# Latihan   : 5-Shortest Path
#================================================================

import heapq

# 1. Representasi graph berbobot antar kota menggunakan dictionary
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

# 2. Fungsi Dijkstra
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Jika rute baru memberikan jarak terpendek, maka update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return distances

# 3. Input node awal
node_awal = 'Bogor'
hasil = dijkstra(graph, node_awal)

# 4. Output jarak terpendek
print(f"Jarak terpendek dari {node_awal}:")
for node, distance in hasil.items():
    print(f"{node_awal} -> {node} = {distance}")

# ==========================================================
# Jawaban Analisis:
# 1. Node awal yang digunakan apa?
#    Jawab: Bogor.
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
#    Jawab: Depok (jarak = 2).
# 3. Node mana yang memiliki jarak paling besar dari node awal?
#    Jawab: Bandung (jarak = 8).
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
#    Jawab: Dijkstra menginisialisasi jarak Bogor = 0 dan kota lain tak terhingga. Pertama, mengeksplorasi tetangga Bogor, yaitu Jakarta(5) dan Depok(2). Karena Depok lebih kecil, kota ini dieksplorasi selanjutnya. Dari Depok, algoritma mengupdate jarak ke Jakarta menjadi 4 (karena Bogor->Depok->Jakarta = 2+2) dan menemukan rute ke Bandung sebesar 8 (Bogor->Depok->Bandung = 2+6). Saat Jakarta dieksplorasi, jalur Jakarta ke Bandung menghasilkan nilai 4+7=11, karena lebih besar dari nilai yang sudah tercatat (8), rute ini diabaikan. Hasil akhir jarak optimal telah ditemukan.