#================================================================
# Nama  : Najla Septian Putri
# NIM   : J0403251010
# Kelas : B/P1
# Praktikum 12 - Graph II: Shortest Path
#================================================================

# Graph dengan contoh bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    # Menyimpan jarak minimum, diatur menjadi tak hingga (infinity) di awal
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Melakukan relaksasi berulang sebanyak jumlah node dikurangi 1
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika ditemukan jalur baru yang memiliki jarak lebih kecil, lakukan update
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    
    return distances

hasil = bellman_ford(graph, 'A')
print(hasil)

# ==========================================================
# PENJELASAN 
# ==========================================================
# 1. Tujuan Program: 
#    Program ini mengimplementasikan algoritma Bellman-Ford untuk mencari 
#    jarak terpendek dari node awal ('A') ke semua node lain. Algoritma ini 
#    dirancang khusus sehingga mampu menangani graf yang memiliki edge 
#    berbobot negatif (seperti edge C -> B dengan bobot -2 pada kode).
#
# 2. Cara Kerja Algoritma:
#    - Inisialisasi: Sama halnya dengan Dijkstra, semua jarak awal diatur 
#      menjadi tak terhingga (float('inf')), dan jarak node awal menjadi 0.
#    - Relaksasi Berulang: Bellman-Ford tidak menggunakan priority queue. 
#      Sebagai gantinya, algoritma ini melakukan iterasi untuk mengecek dan 
#      memperbarui seluruh edge (relaksasi) yang ada di dalam graf.
#    - Jumlah Iterasi: Proses relaksasi seluruh edge ini diulang terus-menerus 
#      sebanyak (jumlah node dikurangi 1) kali. Hal ini memastikan bahwa 
#      akumulasi jarak terpendek sudah menyebar ke seluruh graf, meskipun ada 
#      bobot yang bernilai negatif dan mengurangi total jarak.
#
# 3. Keunggulan & Kekurangan: 
#    Keunggulannya adalah fleksibilitas dalam menangani bobot negatif. Namun, 
#    kekurangannya adalah waktu komputasinya (kompleksitas waktu) lebih lambat 
#    jika dibandingkan dengan algoritma Dijkstra karena ia harus mengevaluasi 
#    seluruh sisi (edge) berulang kali.