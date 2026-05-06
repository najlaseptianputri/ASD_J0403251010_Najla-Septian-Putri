#================================================================
# Nama      : Najla Septian Putri
# NIM       : J0403251010
# Kelas     : B/P1
# Praktikum 12 - Graph II: Shortest Path
# Latihan 4 : Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma : Dijkstra
#================================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

hasil = dijkstra(graph, 'Gerbang')
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# ==========================================================
# Jawaban Analisis:
# 1. Lokasi mana yang paling dekat dari Gerbang?
#    Jawab: Kantin (2 menit)
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
#    Jawab: 7 menit (melalui Gerbang -> Kantin -> Lab -> Aula)
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
#    Jawab: Tidak. Misalnya jalur Gerbang -> Kantin -> Aula secara langsung memakan waktu 2+7=9 menit. Namun, jika kita menggunakan jalur memutar melewati Lab (Gerbang -> Kantin -> Lab -> Aula), waktu tempuhnya hanya 2+4+1=7 menit.
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
#    Jawab: Karena kasus ini merepresentasikan waktu (yang selalu bernilai positif) dan tidak ada bobot waktu negatif. Dijkstra sangat efisien dalam menyelesaikan permasalahan pencarian rute terpendek pada situasi yang tidak memiliki bobot negatif.