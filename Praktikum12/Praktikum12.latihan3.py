#================================================================
# Nama      : Najla Septian Putri
# NIM       : J0403251010
# Kelas     : B/P1
# Praktikum 12 - Graph II: Shortest Path
# Latihan 3 : Implementasi Bellman-Ford
#================================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    
    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    
    return distances

hasil = bellman_ford(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# ==========================================================
# Jawaban Analisis:
# 1. Berapa bobot langsung dari A ke B?
#    Jawab: 5
# 2. Berapa total bobot jalur A -> C -> B?
#    Jawab: 2 (karena 4 + (-2) = 2)
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
#    Jawab: Jalur A -> C -> B.
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
#    Jawab: Karena algoritma ini melakukan relaksasi semua edge secara berulang sebanyak n-1 kali, sehingga mampu menangkap dan menyesuaikan perhitungan apabila ada bobot negatif yang dapat menurunkan total jarak.
# 5. Apa yang dimaksud dengan proses relaksasi edge?
#    Jawab: Proses mengevaluasi edge (jalur) untuk memastikan apakah total jarak yang melalui edge tersebut memberikan jarak terpendek yang lebih baik dibanding nilai yang telah tercatat sebelumnya, dan memperbaruinya jika ya.
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
#    Jawab: Dijkstra menggunakan pendekatan greedy (lebih cepat namun tidak bisa menangani bobot negatif), sementara Bellman-Ford menggunakan pendekatan relaksasi berulang (lebih lambat tetapi bisa menangani graph dengan bobot negatif).