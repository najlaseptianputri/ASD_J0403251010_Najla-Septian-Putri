#-------------------------------------------------------
# Nama      : Najla Septian Putri
# NIM       : J0403251010 
# Kelas     : B/P1
# Latihan 5 
# Praktikum 13 - Graph III: Spanning Tree
#-------------------------------------------------------

# Deskripsi: 
# Membangun Minimum Spanning Tree (MST) untuk Jaringan Jalan Antar Kota.
# Program ini menggunakan Algoritma Kruskal untuk mencari jalur penghubung
# antar simpul (kota) dengan total bobot (jarak) paling minimum.

# 1. REPRESENTASI WEIGHTED GRAPH
# Format data: (bobot, kota1, kota2)
# Bobot diletakkan di awal tuple agar mempermudah proses sorting.
jalan_kota = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# 2. IMPLEMENTASI ALGORITMA KRUSKAL
# Langkah A: Mengurutkan semua edge berdasarkan bobot terkecil (Greedy approach)
jalan_kota.sort()

mst_jalan = []          # List untuk menampung jalan yang terpilih
total_bobot_mst = 0     # Variabel akumulasi bobot
connected_cities = set() # Set untuk melacak kota yang sudah terhubung

# Langkah B: Iterasi dan seleksi edge
for bobot, u, v in jalan_kota:
    # Syarat seleksi: Jika salah satu atau kedua kota belum masuk dalam jaringan MST,
    # maka jalan tersebut diambil untuk menghindari siklus sederhana.
    if u not in connected_cities or v not in connected_cities:
        mst_jalan.append((u, v, bobot))
        total_bobot_mst += bobot
        connected_cities.add(u)
        connected_cities.add(v)

# 3. OUTPUT MST
print("="*45)
print("HASIL JARINGAN JALAN MST (ANTAR KOTA):")
print("-"*45)
for edge in mst_jalan:
    print(f"Jalur: {edge[0]:<7} - {edge[1]:<7} | Bobot: {edge[2]}")

# 4. OUTPUT TOTAL BOBOT MINIMUM
print("-"*45)
print(f"TOTAL BOBOT MINIMUM MST = {total_bobot_mst}")
print("="*45)

#-------------------------------------------------------
# PENJELASAN ANALISIS 
# 1. Kasus yang dipilih: Kasus 1 (Jaringan Jalan Antar Kota).
# 2. Algoritma yang digunakan: Algoritma Kruskal (dengan pendekatan pengurutan sisi).
# 3. Edge yang dipilih dalam MST: 
#   - (Bogor - Depok, bobot 2)
#   - (Depok - Jakarta, bobot 3)
#   - (Depok - Bandung, bobot 4)
# 4. Total bobot MST: 9.
# 5. Mengapa edge tertentu tidak dipilih? 
#    Edge (Bogor-Jakarta, bobot 5) dan (Jakarta-Bandung, bobot 6) tidak dipilih 
#    karena kota-kota tersebut sudah terhubung melalui jalur lain yang memiliki 
#    bobot lebih kecil (via Depok). Algoritma Kruskal selalu memprioritaskan 
#   biaya termurah selama tidak membentuk sirkuit yang tidak perlu.
#-------------------------------------------------------