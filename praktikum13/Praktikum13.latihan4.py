#-------------------------------------------------------
# Nama      : Najla Septian Putri
# NIM       : J0403251010 
# Kelas     : B/P1
# Latihan 4 
# Praktikum 13 - Graph III: Spanning Tree
#-------------------------------------------------------

# Deskripsi: Menentukan jaringan kabel antar gedung dengan biaya minimum 
# Menggunakan Algoritma Kruskal untuk penyelesaian 

# Representasi weighted graph (bobot, node1, node2) 
gedung_edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# Langkah Kruskal: Urutkan edge
# Ini adalah karakteristik "Greedy" dari algoritma Kruskal.
gedung_edges.sort()

# Inisialisasi variabel pendukung
mst_kabel = []      # List untuk menyimpan jalur kabel yang terpilih masuk MST
total_biaya = 0     # Akumulator untuk menghitung total biaya minimum
terhubung = set()   # Set untuk melacak gedung mana saja yang sudah terkoneksi

for biaya, u, v in gedung_edges:
    # Memastikan tidak membentuk cycle sederhana
    if u not in terhubung or v not in terhubung:
        mst_kabel.append((u, v, biaya)) # Tambahkan sisi tersebut ke dalam daftar MST
        total_biaya += biaya            # Tambahkan biaya sisi tersebut ke total biaya
        # Tandai kedua gedung sebagai gedung yang sudah terhubung
        terhubung.add(u)
        terhubung.add(v)

# Output hasil sesuai ketentuan 
print("Jaringan Kabel Minimum (Gedung):")
for edge in mst_kabel:
    print(f"{edge[0]} - {edge[1]} : Biaya {edge[2]}")
print("Total biaya minimum =", total_biaya)

# ==========================================================
# JAWABAN ANALISIS
# 1. Algoritma apa yang digunakan? Algoritma Kruskal.
# 2. Edge mana saja yang dipilih? (C-D, biaya 1), (A-C, biaya 2), (B-D, biaya 3).
# 3. Berapa total biaya minimum? 6.
# 4. Mengapa MST cocok digunakan pada kasus ini? Karena tujuannya adalah menghubungkan 
#    seluruh gedung (node) agar saling terkoneksi dengan total biaya (bobot) yang paling kecil.
# ==========================================================