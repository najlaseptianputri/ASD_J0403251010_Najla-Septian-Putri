#-------------------------------------------------------
# Nama      : Najla Septian Putri
# NIM       : J0403251010 
# Kelas     : B/P1
# Latihan 1
# Praktikum 13 - Graph III: Spanning Tree
#-------------------------------------------------------

# Ini adalah representasi graf asli yang masih memiliki siklus (cycle).
# Contohnya: A-C-D-A membentuk sebuah segitiga/siklus.
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Spanning tree adalah subset dari graf di atas. 
# Syarat utamanya: Semua node (A, B, C, D) harus terhubung, tetapi tidak boleh ada siklus.
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# Menampilkan seluruh sisi yang ada pada graf asli
print("Edge pada graph:")
for edge in edges:
    print(edge)

# Menampilkan sisi yang dipilih untuk menjadi Spanning Tree
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

# Menampilkan perbandingan jumlah edge 
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

#-------------------------------------------------------
# JAWABAN ANALISIS
# 1. Perbedaan graph awal dan spanning tree: Graph awal dapat memiliki cycle (siklus), 
#    sedangkan spanning tree adalah subgraph yang menghubungkan semua node tanpa cycle.
# 2. Mengapa spanning tree tidak boleh memiliki cycle: Karena cycle menyebabkan penggunaan 
#    edge berlebih dan meningkatkan biaya total tanpa menambah konektivitas antar node.
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit: Karena spanning tree hanya 
#    menggunakan jumlah minimum edge untuk menghubungkan seluruh node, yaitu (jumlah node - 1).
#-------------------------------------------------------